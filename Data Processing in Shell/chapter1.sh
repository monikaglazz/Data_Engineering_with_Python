# 1
#  check if curl is installed

man curl

# flags for curl
# -O -> flag to save a file with original name
# -o -> flag to make a new name for file
# -L -> flag redirects HTTP URL if a 300 error 
# -C -> resumes a previous file transfer if times runs out

curl -O https://websitename.com/datafilename.txt

curl -o renameddatafilename.txt https://websitename.com/datafilename.txt

curl -L -O -C https://websitename.com/datafilename[001-100].txt

# 2
# download multiple files 

curl -O https://websitename.com/datafilename*.txt

curl -O https://websitename.com/datafilename[001-100].txt

curl -O https://websitename.com/datafilename[001-100:10].txt

# 3
# Download and rename the file in the same step
curl -o Spotify201812.zip -L https://assets.datacamp.com/production/repositories/4180/datasets/eb1d6a36fa3039e4e00064797e1a1600d267b135/201812SpotifyData.zip

# 4
# Download all 100 data files
curl -O https://s3.amazonaws.com/assets.datacamp.com/production/repositories/4180/datasets/files/datafile[001-100].txt

# Print all downloaded files to directory
ls datafile*.txt

# 5
# check if Wget is installed

which wget

# flags for wget
# -b -> go to background after starup
# -q -> turn off the wget output
# -c -> resume broken download
# -i -> download URLs fro file one by one
# --limit-rate -> set a banwidth limit 
# --wait -> enforcing a mandatory wait time between file downloads

wget -bqc https://websitename.com/datafilename.txt

# 6
# Fill in the two option flags 
wget -cb https://assets.datacamp.com/production/repositories/4180/datasets/eb1d6a36fa3039e4e00064797e1a1600d267b135/201812SpotifyData.zip

# Verify that the Spotify file has been downloaded
ls 

# Preview the log file 
cat wget-log

# 7
# View url_list.txt to verify content
cat url_list.txt

# Create a mandatory 1 second pause between downloading all files in url_list.txt
wget --wait=1 -i url_list.txt

# Take a look at all files downloaded
ls

# 8
# Use curl, download and rename a single file from URL
curl -o Spotify201812.zip -L https://assets.datacamp.com/production/repositories/4180/datasets/eb1d6a36fa3039e4e00064797e1a1600d267b135/201812SpotifyData.zip

# Unzip, delete, then re-name to Spotify201812.csv
unzip Spotify201812.zip && rm Spotify201812.zip
mv 201812SpotifyData.csv Spotify201812.csv

# View url_list.txt to verify content
cat url_list.txt

# Use Wget, limit the download rate to 2500 KB/s, download all files in url_list.txt
wget --limit-rate=2500k -i url_list.txt

# Take a look at all files downloaded
ls
