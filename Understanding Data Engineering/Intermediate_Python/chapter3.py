import numpy as np
import pandas as pd

# 1

# Comparison of booleans
print(True == False)

# Comparison of integers
print(-5*15 != 75)

# Comparison of strings
print("pyscript" == "PyScript")

# Compare a boolean with an integer
print(True == 1)

# 2

# Comparison of integers
x = -3 * 6
print(x >= -10)

# Comparison of strings
y = "test"
print('test' <= y)

# Comparison of booleans
print(True > False)

# 3

my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house >= 18)

# my_house less than your_house
print(my_house < your_house)

# 4

# Define variables
my_kitchen = 18.0
your_kitchen = 14.0

# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen > 10 and my_kitchen < 18)

# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen < 14 or my_kitchen > 17)

# Double my_kitchen smaller than triple your_kitchen?
print(2*my_kitchen < 3*your_kitchen)

# 5

my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))

# 6

# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit":
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else:
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15:
    print("big place!")
elif area > 10:
    print("medium size, nice!")
else:
    print("pretty small.")

# 7

cars = pd.read_csv('cars.csv', index_col=0)

# 8

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars['cars_per_cap']
many_cars = cpc > 500
car_maniac = cars[many_cars]

# Print car_maniac
print(car_maniac)

# 9

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]
