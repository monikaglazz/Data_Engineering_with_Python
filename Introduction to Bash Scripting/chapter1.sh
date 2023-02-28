#!/usr/bash

# 1
# count the number of lines in the book that contain either the 
# character 'Sydney Carton' or 'Charles Darnay'
cat two_cities.txt | egrep "Sydney Carton | Charles Darnay" | wc -l

# 2
# create a Bash script from a shell piped command which will 
# aggregate to see how many times each team has won
cat soccer_scores.csv | cut -d "," -f 2 | tail -n +2 | sort | uniq -c

# 3
# Create a pipe using sed twice to change the team Cherno to Cherno City 
# first, and then Arda to Arda United
cat soccer_scores.csv | sed 's/Cherno/Cherno City/g' | sed 's/Arda/Arda United/g' > soccer_scores_edited.csv

# 4
# Echo the first and second ARGV arguments
echo $1 
echo $2

# Echo out the entire ARGV array
echo $@

# Echo out the size of ARGV
echo $#

# 5
# You need to extract salary figures for recent hires
# Echo the first ARGV argument
echo $1 

# Cat all the files
# Then pipe to grep using the first ARGV argument
# Then write out to a named csv using the first ARGV argument
cat hire_data/* | grep "$1" > "$1".csv