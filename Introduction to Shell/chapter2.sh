# check the content of file

cat course.txt

# print large files and then scroll through the output, one page is displayed at a time
# spacebar -> move between pages
# :n -> move to the next file
# :p -> to go back to the previous one
# :q -> to quit

less seasonal/spring.csv seasonal/summer.csv

# print first 10 lines of file

head people/agarwal.txt

# auto-complete the path with tab. If the path is ambiguous, 
# such as seasonal/s, pressing tab a second time will display a list of possibilities

# print first n lines of file

head -n 3 seasonal/summer.csv

# see everything underneath a directory, no matter how deeply nested it is

ls -R -F ~

# get the manual for command

man head

# get columns from file
# select columns 2 through 5 and columns 8, using comma as the separator".
# -f (meaning "fields") to specify columns
# -d (meaning "delimiter") to specify the separator.

cut -f 2-5,8 -d , values.csv

# display history of commands 

history

# select lines according to what they contain
# -c -> print a count of matching lines rather than the lines themselves
# -h -> do not print the names of files when searching multiple files
# -i -> ignore case (e.g., treat "Regression" and "regression" as matches)
# -l -> print the names of files that contain matches, not the matches
# -n -> print line numbers for matching lines
# -v -> invert the match, i.e., only show lines that don't match

grep -c bicuspid seasonal/winter.csv
