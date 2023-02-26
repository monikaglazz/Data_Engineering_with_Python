# save output to the file

tail -n 5 seasonal/winter.csv > last.csv

# count
#  -l -> lines
#  -c -> characters
#  -w -> words

grep 2017-07 seasonal/spring.csv | wc -l

# sort data (ascending and alphabeticaly default)
# -n -> numerically
# -r -> reverse
# -b -> ignore leading blanks
# -f -> fold case

cut -d , -f 2 seasonal/summer.csv | grep -v Tooth | sort -r

# remove duplicated lines when they are one after one

cut -d , -f 2 seasonal/winter.csv | grep -v Tooth | sort | uniq -c

# stop running program -> ctrl + c