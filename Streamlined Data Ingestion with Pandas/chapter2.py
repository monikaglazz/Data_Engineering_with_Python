# Load pandas as pd
import pandas as pd

# Load matplotlib as plt
import matplotlib as plt


#### SPREADSHEETS ####


# 1

# Read spreadsheet and assign it to survey_responses
survey_responses = pd.read_excel('fcc_survey.xlsx')



# 2

# Create string of lettered columns to load
col_string = 'AD,AW:BA' 

# Load data skipping the first 2 rows
survey_responses2 = pd.read_excel("fcc_survey_headers.xlsx", 
                        usecols = col_string, 
                        skiprows = 2)



# 3

# Create df from second worksheet by referencing its position
responses_2017 = pd.read_excel("fcc_survey.xlsx",
                               sheet_name = 1)



# 4

# Create df from second worksheet by referencing its name
responses_2017 = pd.read_excel("fcc_survey.xlsx",
                               sheet_name = '2017')



# 5

# Load both the 2016 and 2017 sheets by name
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                sheet_name = ['2016','2017'])

# Load all sheets in the Excel file
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                sheet_name = [0, '2017'])

# Load all sheets in the Excel file
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                sheet_name = None)



# 6

# All sheets have been read into the ordered dictionary responses, 
# where sheet names are keys and dataframes are values
responses = {2016: survey_responses, 2017: responses_2017}

# Create an empty dataframe
all_responses = pd.DataFrame()

# Set up for loop to iterate through values in responses
for df in responses.values():
  # Print the number of rows being added
  print("Adding {} rows".format(df.shape[0]))
  # Append df to all_responses, assign result
  all_responses = all_responses.append(df)



# 7

# Create string of lettered columns to load
cols = 'AP,AH,AI,AK,AM'

# Create dataframe from excel using only selected columns
survey_data = pd.read_excel("fcc_survey.xlsx", 
                            sheet_name = '2017',
                            usecols = cols, 
                            skiprows = 2)

# Count NA values in each column
print(survey_data.isna().sum())

# Set dtype to load appropriate column(s) as Boolean data
survey_data = pd.read_excel("fcc_survey_subset.xlsx",
                            sheet_name = '2017',
                            dtype={'HasDebt': bool})

# View financial burdens by Boolean group
print(survey_data.groupby('HasDebt').sum())



# 8

# Set dtype to load appropriate column(s) as Boolean data
survey_data = pd.read_excel("fcc_survey.xlsx", 
                            usecols = cols, 
                            sheet_name = '2017',
                            skiprows = 2,
                            dtype={'HasDebt': bool})

# View financial burdens by Boolean group
print(survey_data.groupby('HasDebt').sum())



# 9

# Load file with Yes as a True value and No as a False value
survey_subset = pd.read_excel("fcc_survey.xlsx",
                            sheet_name = 'sub',
                              dtype={"HasDebt": bool,
                              "AttendedBootCampYesNo": bool},
                              true_values = ["Yes"],
                              false_values = ["No"])




# 10

# Load file, with Part1StartTime parsed as datetime data
survey_data = pd.read_excel("fcc_survey.xlsx",
                            parse_dates=["Part1StartTime"])

# Print first few values of Part1StartTime
print(survey_data.Part1StartTime.head())



# 11

# Create dict of columns to combine into new datetime column
datetime_cols = {"Part2Start": ['Part2StartDate','Part2StartTime']}

# Load file, supplying the dict to parse_dates
survey_data = pd.read_excel("fcc_survey_dts.xlsx",
                            parse_dates=datetime_cols)

# View summary statistics about Part2Start
print(survey_data.Part2Start.describe())



# 12

# Parse datetimes and assign result back to Part2EndTime
survey_data["Part2EndTime"] = pd.to_datetime(survey_data["Part2EndTime"],
                                   format='%m%d%Y %H:%M:%S')


# Print first few values of Part2EndTime
print(survey_data.Part2EndTime.head())