# 1
# execute the sql query on sql database

sql2csv --db "sqlite:///SpotifyDatabase.db" \
        --query "SELECT * FROM Spotify_Popularity" \
        > Spotify_Popularity.csv

# 2
# Verify database name 
ls

# Save query to new file Spotify_Popularity_5Rows.csv
sql2csv --db "sqlite:///SpotifyDatabase.db" \
        --query "SELECT * FROM Spotify_Popularity LIMIT 5" \
        > Spotify_Popularity_5Rows.csv

# Verify newly created file
ls

# Print preview of newly created file
csvlook Spotify_Popularity_5Rows.csv

# 3
# Re-direct output to new file: ShortestSong.csv
csvsql --query "SELECT * FROM Spotify_MusicAttributes ORDER BY duration_ms LIMIT 1" \
	Spotify_MusicAttributes.csv > ShortestSong.csv
    
# Preview newly created file 
csvlook ShortestSong.csv

# 4
# Preview CSV file
ls

# Store SQL query as shell variable
sqlquery="SELECT * FROM Spotify_MusicAttributes ORDER BY duration_ms LIMIT 1"

# Apply SQL query to Spotify_MusicAttributes.csv
csvsql --query "$sqlquery" Spotify_MusicAttributes.csv

# 5
# Store SQL query as shell variable
sql_query="SELECT ma.*, p.popularity FROM Spotify_MusicAttributes ma INNER JOIN Spotify_Popularity p ON ma.track_id = p.track_id"

# Join 2 local csvs into a new csv using the saved SQL
csvsql --query "$sql_query" Spotify_MusicAttributes.csv Spotify_Popularity.csv > Spotify_FullData.csv

# Preview newly created file
csvstat Spotify_FullData.csv

# 6
# Preview file
ls

# Upload Spotify_MusicAttributes.csv to database
csvsql --db "sqlite:///SpotifyDatabase.db" --insert Spotify_MusicAttributes.csv

# Store SQL query as shell variable
sqlquery="SELECT * FROM Spotify_MusicAttributes"

# Apply SQL query to re-pull new table in database
sql2csv --db "sqlite:///SpotifyDatabase.db" --query "$sqlquery" 

# 7
# Store SQL for querying from SQLite database 
sqlquery_pull="SELECT * FROM SpotifyMostRecentData"

# Apply SQL to save table as local file 
sql2csv --db "sqlite:///SpotifyDatabase.db" --query "$sqlquery_pull" > SpotifyMostRecentData.csv

# Store SQL for UNION of the two local CSV files
sqlquery_union="SELECT * FROM SpotifyMostRecentData UNION ALL SELECT * FROM Spotify201812"

# Apply SQL to union the two local CSV files and save as local file
csvsql 	--query "$sqlquery_union" SpotifyMostRecentData.csv Spotify201812.csv > UnionedSpotifyData.csv

# Push UnionedSpotifyData.csv to database as a new table
csvsql --db "sqlite:///SpotifyDatabase.db" --insert UnionedSpotifyData.csv
