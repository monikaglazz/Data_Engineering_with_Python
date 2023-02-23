 # Import pandas with the alias pd
import pandas as pd

#### FLAT FILES ####

# 1

# Read the CSV and assign it to the variable data
data = pd.read_csv("vt_tax_data_2016.csv")



# 2

# Load TSV using the sep keyword argument to set delimiter
data = pd.read_csv('vt_tax_data_2016.tsv', sep = '\t')



# 3

# Create list of columns to use
cols = ['zipcode', 'agi_stub', 'mars1', 'MARS2', 'NUMDEP']

# Create dataframe from csv using only selected columns
data = pd.read_csv("vt_tax_data_2016.csv", usecols = cols)



# 4

# Create dataframe of first 500 rows with labeled columns
vt_data_first500 = pd.read_csv("vt_tax_data_2016.csv", nrows=500)

# Create dataframe of next 500 rows with labeled columns
vt_data_next500 = pd.read_csv("vt_tax_data_2016.csv", 
                       		  nrows=500,
                       		  skiprows=500,
                       		  header=None,
                       		  names=list(vt_data_first500))



#### ERRORS AND MISSING DATA ####



# 5

# Load csv with no additional arguments
data = pd.read_csv("vt_tax_data_2016.csv")

# Print the data types
print(data.dtypes)



# 6

# Create dict specifying data types for agi_stub and zipcode
data_types = {"agi_stub" : "category",
			  "zipcode" : str}

# Load csv using dtype to set correct data types
data = pd.read_csv("vt_tax_data_2016.csv", dtype = data_types)



# 7

# Create dict specifying that 0s in zipcode are NA values
null_values = {"zipcode" : 0}

# Load csv using na_values keyword argument
data = pd.read_csv("vt_tax_data_2016.csv", 
                   na_values = null_values)

# View rows with NA ZIP codes
print(data[data.zipcode.isna()])



# 8

# Handling corrupted data
try:
  data = pd.read_csv("vt_tax_data_2016_corrupt.csv", 
                     error_bad_lines=False, 
                     warn_bad_lines=True)  
except pd.errors.ParserError:
    print("Your data contained rows that could not be parsed.")
