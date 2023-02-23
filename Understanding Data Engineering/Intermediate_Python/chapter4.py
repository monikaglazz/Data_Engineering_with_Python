import pandas as pd

# 1

# Initialize offset
offset = -6

# Code the while loop
while offset != 0:
    print("correcting...")
    if offset > 0:
        offset = offset - 1
    else:
        offset = offset + 1
    print(offset)

#  2

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for i in areas:
    print(i)

# 3

# Change for loop to use enumerate() and update print()
for x, y in enumerate(areas):
    print("room", x, ':', y)

# 4

# Code the for loop
for index, area in enumerate(areas):
    print("room " + str(index + 1) + ": " + str(area))


# 5

# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Build a for loop from scratch
for i in range(len(house)):
    print('the', house[i][0], 'is', house[i][1], 'sqm')


# 6

# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
          'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'austria': 'vienna'}

# Iterate over europe
for key, value in europe.items():
    print("the capital of", key, "is", value)

# 7

cars = pd.read_csv('cars.csv', index_col=0)

# Iterate over rows of cars
for lab, row in cars.iterrows():
    print(lab)
    print(row)

# 8

# Adapt for loop
for lab, row in cars.iterrows():
    print(lab + ":", str(row['cars_per_cap']))

# 9

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, 'COUNTRY'] = row['country'].upper()

# 10

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)
