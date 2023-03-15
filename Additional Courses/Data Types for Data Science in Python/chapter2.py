# Import the python CSV module
import csv

# 1

female_baby_names_2012 = {44: 'RIVKY', 26: 'JULIA', 43: 'TOBY', 37: 'MALKY', 19: 'ABIGAIL', 25: 'ZOE', 42: 'PENELOPE', 39: 'MALKA', 33: 'SHAINDY', 36: 'MADISON', 35: 'GITTY', 32: 'STELLA', 41: 'MADELINE', 7: 'CHAYA', 38: 'EVA', 18: 'ELIZABETH', 30: 'GRACE', 34: 'FAIGY', 14: 'SARA', 45: 'NICOLE', 20: 'ALEXANDRA', 12: 'EMILY', 29: 'HANNAH', 1: 'EMMA', 40: 'ALEXA', 28: 'GABRIELLA', 24: 'RIVKA', 4: 'SOPHIA', 5: 'ESTHER', 27: 'SOPHIE', 22: 'LILY', 10: 'MIRIAM', 8: 'AVA', 9: 'CHANA', 13: 'MIA', 6: 'RACHEL', 17: 'MAYA', 31: 'AVERY', 11: 'ELLA', 23: 'SOFIA', 3: 'SARAH', 21: 'VICTORIA',
                          16: 'ISABELLA', 2: 'LEAH', 15: 'CHARLOTTE', 46: 'VIOLET', 47: 'NATALIE', 69: 'LILIANA', 62: 'SURY', 71: 'SAVANNAH', 75: 'VERA', 72: 'VANESSA', 48: 'REBECCA', 77: 'SYLVIA', 67: 'TAYLOR', 57: 'VALENTINA', 73: 'SIMONE', 79: 'SHAINA', 53: 'RILEY', 64: 'YIDES', 78: 'SIMA', 51: 'NINA', 74: 'SLOANE', 63: 'NAOMI', 70: 'YAEL', 55: 'SYDNEY', 68: 'ZOEY', 76: 'YEHUDIS', 60: 'FRANCESCA', 49: 'MARIA', 61: 'ZISSY', 65: 'SKYLAR', 59: 'JOSEPHINE', 66: 'VERONICA', 50: 'YITTY', 58: 'TALIA', 52: 'KATHERINE', 54: 'SIENNA', 56: 'VIVIENNE', 81: 'YITTA', 83: 'YARA', 82: 'TZIVIA', 80: 'TZIPORA'}

# Create an empty dictionary: names_by_rank
names_by_rank = {}

# Loop over the girl names
for rank, name in female_baby_names_2012.items():
    # Add each name to the names_by_rank dictionary using rank as the key
    names_by_rank[rank] = name

# Sort the names_by_rank dict by rank in descending order and slice the first 10 items
for rank in sorted(names_by_rank, reverse=True)[:10]:
    # Print each item
    print(names_by_rank[rank])

# 2

names = {44: 'RIVKY', 26: 'JULIA', 43: 'TOBY', 37: 'MALKY', 19: 'ABIGAIL', 25: 'ZOE', 42: 'PENELOPE', 39: 'MALKA', 33: 'SHAINDY', 36: 'MADISON', 35: 'GITTY', 32: 'STELLA', 41: 'MADELINE', 7: 'CHAYA', 38: 'EVA', 18: 'ELIZABETH', 30: 'GRACE', 34: 'FAIGY', 14: 'SARA', 45: 'NICOLE', 20: 'ALEXANDRA', 12: 'EMILY', 29: 'HANNAH', 1: 'EMMA', 40: 'ALEXA', 28: 'GABRIELLA', 24: 'RIVKA', 4: 'SOPHIA', 5: 'ESTHER', 27: 'SOPHIE', 22: 'LILY', 10: 'MIRIAM', 8: 'AVA', 9: 'CHANA', 13: 'MIA', 6: 'RACHEL', 17: 'MAYA', 31: 'AVERY', 11: 'ELLA', 23: 'SOFIA', 3: 'SARAH', 21: 'VICTORIA',
         16: 'ISABELLA', 2: 'LEAH', 15: 'CHARLOTTE', 46: 'VIOLET', 47: 'NATALIE', 69: 'LILIANA', 62: 'SURY', 71: 'SAVANNAH', 75: 'VERA', 72: 'VANESSA', 48: 'REBECCA', 77: 'SYLVIA', 67: 'TAYLOR', 57: 'VALENTINA', 73: 'SIMONE', 79: 'SHAINA', 53: 'RILEY', 64: 'YIDES', 78: 'SIMA', 51: 'NINA', 74: 'SLOANE', 63: 'NAOMI', 70: 'YAEL', 55: 'SYDNEY', 68: 'ZOEY', 76: 'YEHUDIS', 60: 'FRANCESCA', 49: 'MARIA', 61: 'ZISSY', 65: 'SKYLAR', 59: 'JOSEPHINE', 66: 'VERONICA', 50: 'YITTY', 58: 'TALIA', 52: 'KATHERINE', 54: 'SIENNA', 56: 'VIVIENNE', 81: 'YITTA', 83: 'YARA', 82: 'TZIVIA', 80: 'TZIPORA'}

# Safely print rank 7 from the names dictionary
print(names.get(7))

# Safely print the type of rank 100 from the names dictionary
print(type(names.get(100)))

# Safely print rank 105 from the names dictionary or 'Not Found'
print(names.get(105, 'Not Found'))

# 3

boy_names = {2013: {50: 'Logan', 13: 'Henry', 54: 'Yaakov', 47: 'Yitzchok', 49: 'Menachem', 32: 'Luke', 44: 'Aron', 56: 'Omar', 42: 'Aaron', 5: 'Daniel', 43: 'Zachary', 45: 'Luca', 24: 'Anthony', 16: 'Nicholas', 30: 'Leo', 25: 'Isaac', 57: 'Levi', 19: 'Chaim', 51: 'Aiden', 37: 'Christopher', 55: 'Yakov', 33: 'Jackson', 21: 'Liam', 36: 'Joshua', 53: 'Peter', 38: 'Sebastian', 7: 'James', 52: 'Yisroel', 40: 'Eli', 27: 'Andrew', 35: 'Theodore', 8: 'Jacob', 2: 'Joseph', 14: 'Noah', 34: 'Shimon', 46: 'Yehuda', 29: 'Yosef', 22: 'Ryan', 9: 'Jack', 1: 'David', 28: 'Gabriel', 48: 'Owen', 26: 'Oliver', 11: 'William', 31: 'Thomas', 23: 'Lucas', 10: 'Alexander', 39: 'Mason', 4: 'Moshe', 41: 'Nathan', 17: 'Matthew', 12: 'John', 6: 'Benjamin', 20: 'Abraham', 18: 'Adam', 3: 'Michael', 15: 'Samuel', 62: 'Jonah', 61: 'Connor', 60: 'Patrick', 59: 'Shmuel', 58: 'Simon', 79: 'Parker', 82: 'Nicolas', 95: 'Sawyer', 94: 'Yoel', 90: 'Rayan', 73: 'Sean', 85: 'Usher', 92: 'Yossi', 65: 'Nathaniel', 93: 'Wesley', 81: 'Yechiel', 69: 'Hunter', 76: 'Martin', 74: 'Sam', 87: 'Yusuf', 67: 'Tyler', 88: 'Yehoshua', 84: 'Spencer', 83: 'Timothy', 63: 'Zev', 86: 'Rafael', 91: 'Tristan', 89: 'Shaya', 71: 'Lipa', 66: 'Harrison', 68: 'Mark', 75: 'Solomon', 78: 'Wyatt', 80: 'Steven', 64: 'Tzvi', 70: 'Mohamed', 72: 'Mendel', 77: 'Edward', 96: 'Yousef', 100: 'Yitzchak', 99: 'Yeshaya', 97: 'Walter', 98: 'Zalmen'}, 2014: {
    54: 'Aron', 14: 'Henry', 58: 'Miles', 38: 'Andrew', 33: 'Eli', 42: 'Jackson', 51: 'Yitzchok', 56: 'Levi', 57: 'Shmuel', 39: 'Zachary', 5: 'Jacob', 40: 'Owen', 48: 'Asher', 26: 'Lucas', 21: 'Noah', 50: 'Robert', 47: 'Jonathan', 55: 'Mark', 36: 'Mason', 29: 'Anthony', 45: 'Aiden', 37: 'Mordechai', 53: 'Christian', 18: 'Ethan', 52: 'George', 24: 'Theodore', 34: 'Shimon', 30: 'Oliver', 7: 'Alexander', 46: 'Christopher', 22: 'Matthew', 9: 'Samuel', 2: 'David', 11: 'James', 35: 'Luke', 28: 'Yosef', 44: 'Nathan', 20: 'Ryan', 10: 'Jack', 1: 'Joseph', 49: 'Logan', 32: 'Gabriel', 17: 'John', 15: 'Abraham', 19: 'Liam', 16: 'Nicholas', 4: 'Moshe', 13: 'William', 12: 'Adam', 27: 'Thomas', 6: 'Benjamin', 23: 'Chaim', 41: 'Yehuda', 31: 'Max', 3: 'Michael', 25: 'Isaac', 8: 'Daniel', 43: 'Yisroel', 59: 'Shlomo', 60: 'Peter', 90: 'Naftali', 75: 'Shia', 98: 'Yisrael', 88: 'Youssef', 74: 'Oscar', 84: 'Philip', 93: 'Shmiel', 95: 'Naftuli', 68: 'Yakov', 96: 'Yusuf', 89: 'Simcha', 91: 'Ronan', 78: 'Tyler', 72: 'Edward', 92: 'Usher', 69: 'Hunter', 85: 'Timothy', 80: 'Sam', 82: 'Ian', 94: 'Yousef', 66: 'Nathaniel', 87: 'Xavier', 97: 'Yossi', 73: 'Yechiel', 67: 'Yaakov', 86: 'Yehoshua', 81: 'Shaya', 70: 'Vincent', 79: 'Wyatt', 61: 'Sean', 64: 'Gavin', 83: 'Raphael', 65: 'Zev', 62: 'Eliezer', 76: 'Leonardo', 77: 'Victor', 63: 'Solomon', 71: 'Ari', 100: 'Yoel', 101: 'Yahya', 99: 'Shea', 102: 'Yidel'}, 2012: {}}

# Print a list of keys from the boy_names dictionary
print(boy_names.keys())

# Print a list of keys from the boy_names dictionary for the year 2013
print(boy_names[2013].keys())

# Loop over the dictionary
for year in boy_names:
    # Safely print the year and the third ranked name or 'Unknown'
    print(year, boy_names[year].get(3, 'Unknown'))

# 4

names_2011 = {51: 'Owen', 19: 'Andrew', 46: 'Sebastian', 36: 'Isaac', 38: 'Zachary', 52: 'Vincent', 47: 'Mark', 45: 'Yehuda', 34: 'Max', 7: 'Daniel', 30: 'Oliver', 18: 'Anthony', 22: 'Lucas', 53: 'Tyler', 25: 'Thomas', 14: 'John', 48: 'Robert', 23: 'Dylan', 39: 'Leo', 16: 'Henry', 35: 'Shimon', 42: 'Jake', 28: 'Yosef', 37: 'Joshua', 27: 'Menachem', 50: 'George', 49: 'Logan', 56: 'Yitzchok', 55: 'Aidan', 10: 'Jack', 17: 'Chaim', 54: 'Yakov', 9: 'Matthew', 1: 'Michael', 44: 'Yisroel', 15: 'Nicholas', 21: 'Charles', 43: 'Mordechai', 31: 'Noah', 6: 'Moshe', 2: 'Joseph', 41: 'Aiden', 20: 'Liam', 4: 'David', 8: 'Alexander', 24: 'Ryan', 5: 'Benjamin', 33: 'Gabriel',
              12: 'James', 29: 'Luke', 26: 'Ethan', 11: 'Samuel', 40: 'Julian', 3: 'Jacob', 32: 'Eli', 13: 'William', 58: 'Theodore', 61: 'Zev', 63: 'Yaakov', 64: 'Shmuel', 59: 'Peter', 62: 'Nathaniel', 60: 'Solomon', 57: 'Asher', 92: 'Spencer', 90: 'Yitzchak', 82: 'Wyatt', 72: 'Sam', 91: 'Shea', 88: 'Rocco', 70: 'Cole', 68: 'Jayden', 66: 'Tzvi', 89: 'Xavier', 94: 'Yida', 83: 'Tristan', 71: 'Sean', 67: 'Levi', 76: 'Moses', 78: 'Usher', 93: 'Zalmen', 84: 'Louis', 87: 'Yoel', 80: 'Yechiel', 81: 'Shaya', 85: 'Yehoshua', 75: 'Steven', 77: 'Shia', 73: 'Victor', 86: 'Sholom', 79: 'Nicolas', 74: 'Omar', 65: 'Shulem', 69: 'Mohamed', 96: 'Youssef', 97: 'Yonah', 95: 'Yousef'}

# Assign the names_2011 dictionary as the value to the 2011 key of boy_names
boy_names[2011] = names_2011

# Update the 2012 key in the boy_names dictionary
boy_names[2012].update([(1, 'Casey'), (2, 'Aiden')])

# Loop over the years in the boy_names dictionary
for year in boy_names:
    # Sort the data for each year by descending rank and get the lowest one
    lowest_ranked = sorted(boy_names[year], reverse=True)[0]
    # Safely print the year and the least popular name or 'Not Available'
    print(year, boy_names[year].get(lowest_ranked, 'Not Available'))

# 5

female_names = {2013: {7: 'Rachel', 2: 'Emma', 4: 'Sophia', 5: 'Sarah', 9: 'Miriam', 6: 'Leah', 8: 'Chaya', 3: 'Esther', 1: 'Olivia', 10: 'Chana'}, 2014: {10: 'Miriam', 5: 'Emma', 2: 'Esther', 9: 'Ava', 4: 'Leah',
                                                                                                                                                           3: 'Rachel', 7: 'Sarah', 8: 'Sophia', 6: 'Chaya', 1: 'Olivia'}, 2012: {}, 2011: {10: 'Miriam', 5: 'Emma', 2: 'Esther', 9: 'Ava', 4: 'Leah', 3: 'Rachel', 7: 'Sarah', 8: 'Sophia', 6: 'Chaya', 1: 'Olivia'}}

# Remove 2011 from female_names and store it: female_names_2011
female_names_2011 = female_names.pop(2011)

# Safely remove 2015 from female_names with an empty dictionary as the default: female_names_2015
female_names_2015 = female_names.pop(2015, {})

# Delete 2012 from female_names
del female_names[2012]

# Print female_names
print(female_names)

# 6

baby_names = {2013: {7: 'James', 2: 'Joseph', 4: 'Moshe', 5: 'Daniel', 9: 'Jack', 6: 'Benjamin', 8: 'Jacob', 3: 'Michael', 1: 'David', 10: 'Alexander'}, 2014: {
    10: 'Jack', 5: 'Jacob', 2: 'David', 9: 'Samuel', 4: 'Moshe', 3: 'Michael', 7: 'Alexander', 8: 'Daniel', 6: 'Benjamin', 1: 'Joseph'}, 2012: {}}

# Iterate over the 2014 nested dictionary
for rank, name in baby_names[2014].items():
    # Print rank and name
    print(rank, name)

# Iterate over the 2012 nested dictionary
for rank, name in baby_names[2012].items():
    # Print rank and name
    print(rank, name)

# 7

# Check to see if 2011 is in baby_names
if 2011 in baby_names:
    # Print 'Found 2011'
    print('Found 2011')

# Check to see if rank 1 is in 2012
if 1 in baby_names[2012]:
    # Print 'Found Rank 1 in 2012' if found
    print('Found Rank 1 in 2012')
else:
    # Print 'Rank 1 missing from 2012' if not found
    print('Rank 1 missing from 2012')

# Check to see if Rank 5 is in 2013
if 5 in baby_names[2013]:
    # Print 'Found Rank 5'
    print('Found Rank 5')

# 8

baby = {}

# Create a python file object in read mode for the baby_names.csv file: csvfile
csvfile = open('baby_names.csv', 'r')

# Loop over a csv reader on the file object
for row in csv.reader(csvfile):
    # Print each row
    print(row)
    # Add the rank and name to the dictionary
    baby[row[5]] = row[3]

# Print the dictionary keys
print(baby.keys())

# 9

# Create a python file object in read mode for the `baby_names.csv` file: csvfile
csvfile = open('baby_names.csv', 'r')

# Loop over a DictReader on the file
for row in csv.DictReader(csvfile):
    # Print each row
    print(row)
    # Add the rank and name to the dictionary: baby_names
    baby_names[row['RANK']] = row['NAME']

# Print the dictionary keys
print(baby_names.keys())
