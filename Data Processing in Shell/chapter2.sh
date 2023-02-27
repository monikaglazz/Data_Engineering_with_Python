# 1
# install and upgrade csvkit

pip install csvkit
pip install --upgrade csv kit

# get manual

in2csv --help
in2csv -h

# convert files to csv

in2csv SpotifyData.xlsx > SpotifyData.csv

# print sheet names

in2csv -n SpotifyData.xlsx
in2csv --names SpotifyData.xlsx

# convert sheet to csv

in2csv SpotifyData.xlsx --sheet "Worksheet1_Popularity" > Spotify_Popularity.csv

# preview csv file in command line

csvlook Spotify_Popularity.csv

# 2

# Use ls to find the name of the zipped file
ls

# Use Linux's built in unzip tool to unpack the zipped file 
unzip SpotifyData.zip

# Check to confirm name and location of unzipped file
ls

# Convert SpotifyData.xlsx to csv
in2csv SpotifyData.xlsx > SpotifyData.csv

# Print a preview in console using a csvkit suite command 
csvlook SpotifyData.csv 

# 3

# Check to confirm name and location of the Excel data file
ls

# Convert sheet "Worksheet1_Popularity" to CSV
in2csv SpotifyData.xlsx --sheet "Worksheet1_Popularity" > Spotify_Popularity.csv

# Check to confirm name and location of the new CSV file
ls

# Print high level summary statistics for each column
csvstat Spotify_Popularity.csv 

# Check to confirm name and location of the Excel data file
ls

# Convert sheet "Worksheet2_MusicAttributes" to CSV
in2csv SpotifyData.xlsx --sheet "Worksheet2_MusicAttributes" > Spotify_MusicAttributes.csv

# Check to confirm name and location of the new CSV file
ls

# Print preview of Spotify_MusicAttributes
csvlook Spotify_MusicAttributes.csv

# 4
# filter data with:
# csvcut: filters data using column name or position 
# -n / --names -> print all column names
# -c -> return column by position or name

csvcut -c 1 Spotify_MusicAttributes.csv
csvcut -c 2,3 Spotify_MusicAttributes.csv
csvcut -c "danceability","duration_ms" Spotify_MusicAttributes.csv

# csvgrep: filters data by row value through exact match, pattern matching,or even regex
# -m -> exact row value
# -r -> regex pattern
# -f -> path to file

csvgrep -c "track_id" -m 5RCPsfzmEpTXMCTNk7wEfQ Spotify_Popularity.csv


# 5

# Check to confirm name and location of data file
ls

# Print a list of column headers in data file 
csvcut -n Spotify_MusicAttributes.csv

# Print the first column, by position
csvcut -c 1 Spotify_MusicAttributes.csv

# Print the first, third, and fifth column, by position
csvcut -c 1,3,5 Spotify_MusicAttributes.csv

# Print the first column, by name
csvcut -c "track_id" Spotify_MusicAttributes.csv

# Print the track id, song duration, and loudness, by name 
csvcut -c "track_id","duration_ms","loudness" Spotify_MusicAttributes.csv


# 6

# Print a list of column headers in the data 
csvcut -n Spotify_MusicAttributes.csv

# Filter for row(s) where track_id = 118GQ70Sp6pMqn6w1oKuki
csvgrep -c "track_id" -m 118GQ70Sp6pMqn6w1oKuki Spotify_MusicAttributes.csv

# Filter for row(s) where danceability = 0.812
csvgrep -c "danceability" -m 0.812 Spotify_MusicAttributes.csv


# 7
# stack up multiple files together

csvstack Spotify_Rank6.csv Spotify_Rank7.csv > Spotify_AllRanks.csv


# with adding column "group"
csvstack -g "Rank6","Rank7" \ Spotify_Rank6.csv Spotify_Rank7.csv > Spotify_AllRanks.csv

# with adding column "group" as "source"
csvstack -g "Rank6","Rank7" -n "source" \ Spotify_Rank6.csv Spotify_Rank7.csv > Spotify_AllRanks.csv

# chaining
#  ; links command together and runs sequentially
#  && links commands together but runs 2nd command only if 1st succeeds
#  > re-directs the output
#  | uses the output from 1st command as input to 2nd command

# 8

# Stack the two files and save results as a new file
csvstack SpotifyData_PopularityRank6.csv SpotifyData_PopularityRank7.csv > SpotifyPopularity.csv

# Preview the newly created file 
csvlook SpotifyPopularity.csv

# 9

# If csvlook succeeds, then run csvstat 
csvlook Spotify_Popularity.csv && csvstat Spotify_Popularity.csv

# Use the output of csvsort as input to csvlook
csvsort -c 2 Spotify_Popularity.csv | csvlook

# Take top 15 rows from sorted output and save to new file
csvsort -c 2 Spotify_Popularity.csv | head -n 15 > Spotify_Popularity_Top15.csv

# Preview the new file 
csvlook Spotify_Popularity_Top15.csv

# 10

# Convert the Spotify201809 tab into its own csv file 
in2csv Spotify_201809_201810.xlsx --sheet "Spotify201809" > Spotify201809.csv

# Check to confirm name and location of data file
ls

# Preview file preview using a csvkit function
csvlook Spotify201809.csv

# Create a new csv with 2 columns: track_id and popularity
csvcut -c "track_id","popularity" Spotify201809.csv > Spotify201809_subset.csv

# While stacking the 2 files, create a data source column
csvstack -g "Sep2018","Oct2018" Spotify201809_subset.csv Spotify201810_subset.csv > Spotify_all_rankings.csv