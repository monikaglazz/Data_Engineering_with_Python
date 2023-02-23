import csv
from collections import Counter
from datetime import datetime
from collections import defaultdict



# 1 "Read object"

# Create the file object: csvfile
csvfile = open('crime_sampler.csv', 'r')

# Create an empty list: crime_data
crime_data = []

# Loop over a csv reader on the file object
for row in csv.reader(csvfile):

    # Append the date, type of crime, location description, and arrest
    crime_data.append((row[0], row[2], row[4], row[5]))
    
# Remove the first element from crime_data
crime_data.pop(0)

# Print the first 10 records
print(crime_data[:10])


# 2 "Find the Months with the Highest Number of Crimes"

# Create a Counter Object: crimes_by_month
crimes_by_month = Counter()

# Loop over the crime_data list
for crime in crime_data:
    
    # Convert the first element of each item into a Python Datetime Object: date
    date = datetime.strptime(crime[0], '%m/%d/%Y %I:%M:%S %p')
    
    # Increment the counter for the month of the row by one
    crimes_by_month[date.month] += 1
    
# Print the 3 most common months for crime
print(crimes_by_month.most_common(3))



# 3 "Transforming Data Containers to Month and Location"

# Create a dictionary that defaults to a list: locations_by_month
locations_by_month = defaultdict(list)

# Loop over the crime_data list
for crime in crime_data:
    # Convert the first element to a date object
    date = datetime.strptime(crime[0], '%m/%d/%Y %I:%M:%S %p')
    
    # If the year is 2016 
    if date.year == 2016:
        # Set the dictionary key to the month and append the location (fifth element) to the values list
        locations_by_month[date.month].append(crime[4])
    
# Print the dictionary
print(locations_by_month)



# 4 "Find the Most Common Crimes by Location Type by Month in 2016"

# Loop over the items from locations_by_month using tuple expansion of the month and locations
for month, locations in locations_by_month.items():
    # Make a Counter of the locations
    location_count = Counter(locations)
    # Print the month 
    print(month)
    # Print the most common location
    print(location_count.most_common(5))



# 5 "Reading Data with DictReader and Establishing Data Containers"

# Create the CSV file: csvfile
csvfile = open('crime_sampler.csv', 'r')

# Create a dictionary that defaults to a list: crimes_by_district
crimes_by_district = defaultdict(list)

# Loop over a DictReader of the CSV file
for row in csv.DictReader(csvfile):
    # Pop the district from each row: district
    district = row.pop('District')
    # Append the rest of the data to the list for proper district in crimes_by_district
    crimes_by_district[district].append(row)


# 6 "Determine the Arrests by District by Year"

# Loop over the crimes_by_district using expansion as district and crimes
for district, crimes in crimes_by_district.items():
    # Print the district
    print(district)
    
    # Create an empty Counter object: year_count
    year_count = Counter()
    
    # Loop over the crimes:
    for crime in crimes:
        # If there was an arrest
        if crime['Arrest'] == 'true':
            # Convert the Date to a datetime and get the year
            year = datetime.strptime(crime['Date'], '%m/%d/%Y %I:%M:%S %p').year
            # Increment the Counter for the year
            year_count[year] += 1
            
    # Print the counter
    print(year_count)


# 7 "Unique Crimes by City Block"

crimes_by_block = { '049XX S KNOX AVE': ['BATTERY'], '105XX S CORLISS AVE': ['BATTERY'], '054XX N KENMORE AVE': ['SEX OFFENSE'], '040XX S INDIANA AVE': ['BATTERY'], '030XX W POLK ST': ['OTHER OFFENSE'], '068XX S HARPER AVE': ['BURGLARY'], '044XX N KASSON AVE': ['THEFT'], '038XX W 84TH ST': ['BURGLARY'], '054XX S EAST VIEW PARK': ['THEFT'], '047XX S WABASH AVE': ['CRIM SEXUAL ASSAULT'], '003XX W OAK ST': ['CRIMINAL DAMAGE'], '001XX E 76TH ST': ['THEFT'], '027XX N WAYNE AVE': ['THEFT'], '008XX N SEDGWICK ST': ['CRIMINAL TRESPASS'], '024XX N ST LOUIS AVE': ['BURGLARY'], '135XX S AVENUE O': ['BATTERY'], '049XX N BERNARD ST': ['OTHER OFFENSE'], '075XX S COTTAGE GROVE AVE': ['BURGLARY'], '043XX N MELVINA AVE': ['CRIMINAL TRESPASS'], '019XX W EISENHOWER EXPY OB': ['OTHER OFFENSE'], '021XX S HARDING AVE': ['BATTERY'], '071XX S BISHOP ST': ['CRIMINAL DAMAGE'], '038XX W MONTROSE AVE': ['BATTERY'], '043XX N MILWAUKEE AVE': ['CRIMINAL TRESPASS'], '023XX S WENTWORTH AVE': ['THEFT'], '020XX N CLIFTON AVE': ['DECEPTIVE PRACTICE'], '004XX E 110TH PL': ['BATTERY'], '053XX S JUSTINE ST': ['MOTOR VEHICLE THEFT'], '075XX N HOYNE AVE': ['ROBBERY'], '039XX S WELLS ST': ['CRIMINAL DAMAGE'], '065XX S WHIPPLE ST': ['NARCOTICS'], '0000X W TERMINAL ST': ['THEFT', 'THEFT', 'ASSAULT', 'THEFT', 'NARCOTICS', 'PUBLIC PEACE VIOLATION', 'CRIMINAL DAMAGE', 'OTHER OFFENSE', 'CRIMINAL TRESPASS', 'THEFT', 'OTHER OFFENSE', 'THEFT', 'THEFT', 'CRIMINAL TRESPASS', 'THEFT', 'DECEPTIVE PRACTICE', 'THEFT', 'THEFT', 'THEFT', 'CRIMINAL TRESPASS', 'THEFT', 'OTHER OFFENSE', 'THEFT', 'THEFT', 'THEFT', 'THEFT', 'CRIMINAL TRESPASS', 'CRIMINAL DAMAGE', 'CRIMINAL TRESPASS', 'THEFT', 'CRIMINAL TRESPASS'], '066XX S KENWOOD AVE': ['ASSAULT'], '019XX W DIVERSEY PKWY': ['BURGLARY'], '033XX W MONROE ST': ['DECEPTIVE PRACTICE'], '059XX N GLENWOOD AVE': ['BATTERY'], '010XX W 40TH ST': ['THEFT'], '009XX W DIVERSEY PKWY': ['BURGLARY'], '032XX S STEWART AVE': ['THEFT'], '018XX N HALSTED ST': ['MOTOR VEHICLE THEFT'], '125XX S PRINCETON AVE': ['THEFT'], '026XX W 83RD PL': ['BURGLARY'], '082XX S AVALON AVE': ['BURGLARY'], '078XX S ELLIS AVE': ['BATTERY'], '034XX W HURON ST': ['NARCOTICS'], '049XX S PRINCETON AVE': ['BATTERY'], '104XX S MARYLAND AVE': ['MOTOR VEHICLE THEFT'], '072XX N WASHTENAW AVE': ['THEFT'], '026XX N ORCHARD ST': ['THEFT'], '031XX N BERNARD ST': ['ASSAULT'], '005XX E 77TH ST': ['DECEPTIVE PRACTICE'], '023XX N ROCKWELL ST': ['ROBBERY'], '026XX N MERRIMAC AVE': ['DECEPTIVE PRACTICE'], '034XX W 82ND PL': ['THEFT'], '044XX S WALLACE ST': ['NARCOTICS'], '015XX W FARGO AVE': ['MOTOR VEHICLE THEFT'], '024XX N MENARD AVE': ['BURGLARY'], '064XX S NARRAGANSETT AVE': ['BURGLARY'], '018XX S CANALPORT AVE': ['BATTERY'], '006XX W Aldine Ave': ['DECEPTIVE PRACTICE'], '032XX N HALSTED ST': ['MOTOR VEHICLE THEFT'], '093XX S VERNON AVE': ['MOTOR VEHICLE THEFT'], '073XX S FAIRFIELD AVE': ['BATTERY'], '002XX W DE SAIBLE ST': ['CRIMINAL TRESPASS'], '061XX S PEORIA ST': ['BATTERY'], '033XX N BELL AVE': ['THEFT'], '025XX W WILSON AVE': ['CRIMINAL DAMAGE'], '104XX S AVENUE L': ['CRIMINAL DAMAGE'], '102XX S PARNELL AVE': ['OFFENSE INVOLVING CHILDREN'], '099XX S MALTA ST': ['BATTERY'], '057XX S KENWOOD AVE': ['CRIMINAL DAMAGE'], '030XX W WARREN BLVD': ['CRIMINAL DAMAGE'], '048XX S LAFLIN ST': ['CRIMINAL DAMAGE'], '006XX N PINE AVE': ['BATTERY'], '0000X S PAULINA ST': ['ASSAULT'], '049XX N SAWYER AVE': ['NARCOTICS'], '041XX W 79TH ST': ['BATTERY'], '102XX S LOWE AVE': ['BATTERY'], '012XX N AVERS AVE': ['THEFT'], '013XX W TAYLOR ST': ['BATTERY'], '034XX W MELROSE ST': ['DECEPTIVE PRACTICE'], '005XX E 32ND ST': ['CRIMINAL DAMAGE'], '011XX W 104TH PL': ['BATTERY'], '113XX S CALUMET AVE': ['BATTERY'], '015XX W HOLLYWOOD AVE': ['THEFT'], '076XX S UNION AVE': ['OTHER OFFENSE'], '067XX S CALIFORNIA AVE': ['PUBLIC PEACE VIOLATION'], '029XX W 65TH ST': ['OTHER OFFENSE'], '001XX N STATE ST': ['THEFT', 'DECEPTIVE PRACTICE', 'CRIMINAL TRESPASS', 'THEFT', 'THEFT', 'THEFT', 'ROBBERY', 'THEFT', 'THEFT', 'DECEPTIVE PRACTICE', 'THEFT', 'THEFT', 'THEFT', 'DECEPTIVE PRACTICE', 'THEFT', 'THEFT', 'THEFT', 'THEFT', 'ASSAULT', 'THEFT', 'THEFT', 'THEFT', 'THEFT', 'DECEPTIVE PRACTICE', 'DECEPTIVE PRACTICE', 'THEFT', 'THEFT', 'THEFT', 'THEFT', 'THEFT', 'THEFT', 'THEFT', 'THEFT', 'CRIMINAL TRESPASS', 'DECEPTIVE PRACTICE', 'THEFT', 'DECEPTIVE PRACTICE', 'CRIMINAL DAMAGE', 'THEFT', 'THEFT', 'THEFT', 'THEFT', 'THEFT', 'ASSAULT', 'THEFT', 'DECEPTIVE PRACTICE', 'DECEPTIVE PRACTICE', 'THEFT', 'THEFT', 'OTHER OFFENSE', 'THEFT', 'THEFT', 'BATTERY', 'DECEPTIVE PRACTICE', 'THEFT', 'THEFT', 'THEFT', 'DECEPTIVE PRACTICE', 'THEFT'], '001XX E 110TH ST': ['BURGLARY'], '021XX S HOMAN AVE': ['ASSAULT'], '049XX W MAYPOLE AVE': ['ASSAULT'], '033XX W DIVISION ST': ['ASSAULT'], '042XX S ARCHER AVE': ['CRIMINAL DAMAGE'], '019XX W LAKE ST': ['THEFT'], '035XX W 83RD PL': ['THEFT'], '007XX N LAKE SHORE DR': ['MOTOR VEHICLE THEFT'], '006XX W LAWRENCE DR': ['THEFT'], '095XX S JEFFERY AVE': ['BATTERY'], '018XX E 71ST PL': ['OTHER OFFENSE'], '096XX S SANGAMON ST': ['NARCOTICS'], '005XX W ADAMS ST': ['THEFT'], '055XX S HERMITAGE AVE': ['ROBBERY'], '064XX S ALBANY AVE': ['BURGLARY'], '0000X S CENTRAL PARK BLVD': ['NARCOTICS'], '079XX S CHAPPEL AVE': ['CRIMINAL DAMAGE'], '020XX E 79TH ST': ['ASSAULT'], '0000X S HOYNE AVE': ['THEFT'], '038XX W 76TH ST': ['THEFT'], '006XX W 77TH ST': ['CRIMINAL DAMAGE'], '014XX S TALMAN AVE': ['BATTERY'], '059XX S WOOD ST': ['THEFT'], '033XX W WALNUT ST': ['ASSAULT'], '030XX N KEDZIE AVE': ['LIQUOR LAW VIOLATION'], '048XX W WABANSIA AVE': ['OTHER OFFENSE'], '013XX N CENTRAL AVE': ['OTHER OFFENSE'], '041XX W 19TH ST': ['WEAPONS VIOLATION'], '050XX S LARAMIE AVE': ['CRIMINAL DAMAGE'], '060XX S WINCHESTER AVE': ['BATTERY'], '046XX S LAKE SHORE DR SB': ['ROBBERY'], '029XX N HOYNE AVE': ['ASSAULT'], '021XX W CORTEZ ST': ['THEFT'], '007XX W 18TH ST': ['THEFT']}

# Create a unique list of crimes for the first block: n_state_st_crimes
n_state_st_crimes = set(crimes_by_block['001XX N STATE ST'])

# Print the list
print(n_state_st_crimes)

# Create a unique list of crimes for the second block: w_terminal_st_crimes
w_terminal_st_crimes = set(crimes_by_block['0000X W TERMINAL ST'])

# Print the list
print(w_terminal_st_crimes)

# Find the differences between the two blocks: crime_differences
crime_differences = n_state_st_crimes.difference(w_terminal_st_crimes)

# Print the differences
print(crime_differences)
