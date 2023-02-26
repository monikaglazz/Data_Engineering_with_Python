# Unix has a bewildering variety of text editors. 
# We will use a simple one called Nano. 
# If you type nano filename, it will open filename for editing (or create it if it doesn't already exist). 

# Ctrl + K: delete a line.
# Ctrl + U: un-delete a line.
# Ctrl + O: save the file ('O' stands for 'output'). You will also need to press Enter to confirm the filename!
# Ctrl + X: exit the editor.

nano names.txt

# copy files to home directory, 
# select the data records from spring.csv and summer.csv in that order and redirect the output to temp.csv, 
# save three last commands in file steps.txt

cp seasonal/s*.csv ~
grep -h -v Tooth seasonal/s* > temp.csv
history tail -n 3 > steps.txt

# run shell file 

bash file.sh

# Run date-range.sh on all four of the seasonal data files using seasonal/*.csv 
# to match their names, and pipe its output to sort to see that your scripts can be used just like Unix's built-in commands.

bash date-range.sh seasonal/*.csv | sort 