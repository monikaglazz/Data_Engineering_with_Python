# Load pandas as pd
import pandas as pd


#### SPREADSHEETS ####


# Read spreadsheet and assign it to survey_responses
survey_responses = pd.read_excel('fcc_survey.xlsx')

# Create string of lettered columns to load
col_string = 'AD,AW:BA' 

# Load data skipping the first 2 rows
survey_responses2 = pd.read_excel("fcc_survey_headers.xlsx", 
                        usecols = col_string, 
                        skiprows = 2)

