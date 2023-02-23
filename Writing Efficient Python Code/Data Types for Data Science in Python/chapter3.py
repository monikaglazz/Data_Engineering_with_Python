
from collections import Counter, defaultdict, OrderedDict, namedtuple


# 1

stations = ['stationname', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Austin-Forest Park', 'Harlem-Lake', 'Harlem-Lake', 'Harlem-Lake', 'Harlem-Lake', 'Harlem-Lake', 'Harlem-Lake', 'Harlem-Lake', 'Harlem-Lake', 'Harlem-Lake', 'Harlem-Lake', 'Harlem-Lake', 'Harlem-Lake', 'Harlem-Lake', 'Harlem-Lake', 'Harlem-Lake', 'Harlem-Lake', 'Harlem-Lake', 'Harlem-Lake', 'Harlem-Lake', 'Harlem-Lake', 'Harlem-Lake', 'Harlem-Lake', 'Harlem-Lake', 'Harlem-Lake', 'Harlem-Lake', 'Harlem-Lake', 'Harlem-Lake', 'Harlem-Lake', 'Harlem-Lake', 'Harlem-Lake', 'Harlem-Lake', 'Pulaski-Lake', 'Pulaski-Lake', 'Pulaski-Lake', 'Pulaski-Lake', 'Pulaski-Lake', 'Pulaski-Lake', 'Pulaski-Lake', 'Pulaski-Lake', 'Pulaski-Lake', 'Pulaski-Lake', 'Pulaski-Lake', 'Pulaski-Lake', 'Pulaski-Lake', 'Pulaski-Lake', 'Pulaski-Lake', 'Pulaski-Lake', 'Pulaski-Lake', 'Pulaski-Lake', 'Pulaski-Lake', 'Pulaski-Lake', 'Pulaski-Lake', 'Pulaski-Lake', 'Pulaski-Lake', 'Pulaski-Lake', 'Pulaski-Lake', 'Pulaski-Lake', 'Pulaski-Lake', 'Pulaski-Lake', 'Pulaski-Lake', 'Pulaski-Lake', 'Pulaski-Lake', 'Quincy/Wells', 'Quincy/Wells', 'Quincy/Wells', 'Quincy/Wells', 'Quincy/Wells', 'Quincy/Wells', 'Quincy/Wells', 'Quincy/Wells', 'Quincy/Wells',
            'Quincy/Wells', 'Quincy/Wells', 'Quincy/Wells', 'Quincy/Wells', 'Quincy/Wells', 'Quincy/Wells', 'Quincy/Wells', 'Quincy/Wells', 'Quincy/Wells', 'Quincy/Wells', 'Quincy/Wells', 'Quincy/Wells', 'Quincy/Wells', 'Quincy/Wells', 'Quincy/Wells', 'Quincy/Wells', 'Quincy/Wells', 'Quincy/Wells', 'Quincy/Wells', 'Quincy/Wells', 'Quincy/Wells', 'Quincy/Wells', 'Davis', 'Davis', 'Davis', 'Davis', 'Davis', 'Davis', 'Davis', 'Davis', 'Davis', 'Davis', 'Davis', 'Davis', 'Davis', 'Davis', 'Davis', 'Davis', 'Davis', 'Davis', 'Davis', 'Davis', 'Davis', 'Davis', 'Davis', 'Davis', 'Davis', 'Davis', 'Davis', 'Davis', 'Davis', 'Davis', 'Davis', "Belmont-O'Hare", "Belmont-O'Hare", "Belmont-O'Hare", "Belmont-O'Hare", "Belmont-O'Hare", "Belmont-O'Hare", "Belmont-O'Hare", "Belmont-O'Hare", "Belmont-O'Hare", "Belmont-O'Hare", "Belmont-O'Hare", "Belmont-O'Hare", "Belmont-O'Hare", "Belmont-O'Hare", "Belmont-O'Hare", "Belmont-O'Hare", "Belmont-O'Hare", "Belmont-O'Hare", "Belmont-O'Hare", "Belmont-O'Hare", "Belmont-O'Hare", "Belmont-O'Hare", "Belmont-O'Hare", "Belmont-O'Hare", "Belmont-O'Hare", "Belmont-O'Hare", "Belmont-O'Hare", "Belmont-O'Hare", "Belmont-O'Hare", "Belmont-O'Hare", "Belmont-O'Hare", 'Jackson/Dearborn', 'Jackson/Dearborn', 'Jackson/Dearborn', 'Jackson/Dearborn', 'Jackson/Dearborn', 'Jackson/Dearborn', 'Jackson/Dearborn', 'Jackson/Dearborn', 'Jackson/Dearborn', 'Jackson/Dearborn', 'Jackson/Dearborn', 'Jackson/Dearborn', 'Jackson/Dearborn', 'Jackson/Dearborn', 'Jackson/Dearborn', 'Jackson/Dearborn', 'Jackson/Dearborn', 'Jackson/Dearborn', 'Jackson/Dearborn', 'Jackson/Dearborn', 'Jackson/Dearborn', 'Jackson/Dearborn', 'Jackson/Dearborn', 'Jackson/Dearborn', 'Jackson/Dearborn', 'Jackson/Dearborn', 'Jackson/Dearborn', 'Jackson/Dearborn', 'Jackson/Dearborn', 'Jackson/Dearborn', 'Jackson/Dearborn']

# Print the first ten items from the stations list
print(stations[:10])

# Create a Counter of the stations list: station_count
station_count = Counter(stations)

# Print the station_count
print(station_count)


# 3

# Create a Counter of the stations list: station_count
station_count = Counter(stations)

# Find the 5 most common elements
print(station_count.most_common(5))


# 4

entries = [('11/17/2016', 'Dempster-Skokie', '2048'), ('02/19/2016', 'Adams/Wabash', '8447'), ('03/25/2015', 'State/Lake', '10325'), ('05/02/2015', 'Ashland-Lake', '1424'), ('07/11/2015', 'Chicago/Franklin', '2883'), ('06/04/2015', "Addison-O'Hare", '3223'), ('02/11/2016', 'Paulina', '2733'), ('10/08/2016', 'Indiana', '568'), ('08/31/2016', 'Granville', '4124'), ('11/29/2016', 'Pulaski-Orange', '5781'), ('04/17/2015', 'Central-Evanston', '806'), ('03/31/2015', 'Lawrence', '3314'), ('01/06/2016', 'Harlem-Forest Park', '1226'), ('07/03/2015', 'Cicero-Cermak', '1391'), ('02/17/2015', '35th/Archer', '3135'), ('01/31/2016', 'Garfield-Dan Ryan', '1889'), ('02/07/2015', 'Polk', '953'), ('08/13/2016', 'Kedzie-Cermak', '704'), ('12/25/2015', 'Randolph/Wabash', '1954'), ('08/02/2016', 'Western/Milwaukee', '5248'), ('08/04/2016', 'Ashland-Orange', '1568'), ('03/13/2016', 'Oak Park-Forest Park', '422'), ('08/13/2016', 'Pulaski-Forest Park', '1452'), ('05/30/2015', 'Rosemont', '4770'), ('06/22/2016', 'Harlem-Lake', '3749'), ('01/02/2016', 'Randolph/Wabash', '4724'), ('12/28/2015', 'Montrose-Brown', '1699'), ('05/16/2015', 'Main', '906'), ('03/29/2016', 'Pulaski-Lake', '1597'), ('11/15/2015', 'East 63rd-Cottage Grove', '661'), ('11/08/2015', "Belmont-O'Hare", '2674'), ('06/19/2015', 'Armitage', '4528'), ('08/31/2016', 'Foster', '803'), ('11/23/2015', 'Pulaski-Cermak', '1298'), ('04/13/2015', 'Garfield-Dan Ryan', '3788'), ('07/19/2015', 'Central-Lake', '1371'), ('07/14/2015', 'King Drive', '687'), ('04/12/2015', '63rd-Dan Ryan', '1767'), ('01/18/2016', 'Damen-Brown', '1558'), ('08/20/2015', '79th', '7645'), ('05/29/2016', 'Library', '1680'), ('08/16/2015', 'Kedzie-Brown', '1203'), ('08/02/2015', 'Oak Park-Lake', '1044'), ('06/03/2015', 'Pulaski-Forest Park', '2074'), ('09/27/2016', 'Monroe/State', '11896'), ('08/25/2016', 'Addison-Brown', '2423'), ('04/26/2016', 'Jarvis', '1767'), ('05/14/2015', 'Sheridan', '6110'), ('08/20/2015', 'Morse', '4897'), ('01/28/2016',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 'LaSalle', '3432'), ('05/01/2016', 'Clinton-Forest Park', '1315'), ('03/30/2016', 'UIC-Halsted', '7318'), ('08/27/2016', 'Granville', '2715'), ('06/26/2015', 'Belmont-North Main', '12959'), ('05/26/2015', 'Kedzie-Midway', '2637'), ('04/30/2016', 'State/Lake', '5043'), ('08/17/2015', 'Paulina', '2625'), ('07/12/2015', '63rd-Dan Ryan', '2193'), ('09/24/2015', 'Bryn Mawr', '5256'), ('02/28/2016', 'Ashland-Orange', '662'), ('01/07/2016', 'Howard', '5776'), ('12/22/2015', "Addison-O'Hare", '2757'), ('09/06/2015', 'Sox-35th-Dan Ryan', '2778'), ('04/20/2015', 'Cicero-Forest Park', '1403'), ('05/19/2016', '47th-Dan Ryan', '3509'), ('06/22/2016', 'Sox-35th-Dan Ryan', '3778'), ('02/02/2016', 'Kedzie-Midway', '3332'), ('04/10/2016', 'Wellington', '893'), ('06/06/2016', 'Clinton-Lake', '4273'), ('07/13/2015', 'Sedgwick', '3820'), ('10/31/2016', 'Randolph/Wabash', '9522'), ('06/01/2015', '63rd-Dan Ryan', '3183'), ('05/26/2015', 'Jarvis', '1631'), ('11/02/2016', 'Quincy/Wells', '9462'), ('08/06/2015', 'Ridgeland', '1329'), ('03/02/2015', 'Lawrence', '3279'), ('03/22/2016', 'Rosemont', '5979'), ('07/04/2015', 'Washington/Dearborn', '7811'), ('11/13/2016', 'Laramie', '637'), ('01/20/2016', 'Armitage', '4558'), ('10/23/2016', "Addison-O'Hare", '1351'), ('05/23/2016', 'Pulaski-Cermak', '1132'), ('06/26/2016', 'North/Clybourn', '5144'), ('08/08/2015', "Montrose-O'Hare", '1369'), ('07/21/2016', 'Chicago/Milwaukee', '4264'), ('05/20/2015', 'UIC-Halsted', '3227'), ('10/11/2015', '87th', '2911'), ('07/24/2016', 'Chicago/State', '9112'), ('04/04/2016', 'Garfield-South Elevated', '1272'), ('05/17/2015', 'Central Park', '720'), ('03/09/2016', 'Jackson/State', '12445'), ('01/08/2016', 'Dempster', '943'), ('08/19/2016', 'King Drive', '578'), ('01/30/2016', '63rd-Dan Ryan', '2105'), ('08/22/2015', 'Montrose-Brown', '1705'), ('07/23/2015', 'Garfield-Dan Ryan', '4136'), ('11/24/2015', 'Halsted/63rd', '874'), ('02/15/2015', 'Kedzie-Midway', '986'), ('03/14/2016', 'Fullerton', '13623')]

# Create an empty dictionary: ridership
ridership = {}

# Iterate over the entries
for date, stop, riders in entries:
    # Check to see if date is already in the ridership dictionary
    if date not in ridership:
        # Create an empty list for any missing date
        ridership[date] = list()
    # Append the stop and riders as a tuple to the date keys list
    ridership[date].append((stop, riders))

# Print the ridership for '03/09/2016'
print(ridership['03/09/2016'])

# 5

# Create a defaultdict with a default type of list: ridership
ridership = defaultdict(list)

# Iterate over the entries
for date, stop, riders in entries:
    # Use the stop as the key of ridership and append the riders to its value
    ridership[stop].append(riders)

# Print the first 10 items of the ridership dictionary
print(list(ridership.items())[:10])

# 6

# Create an OrderedDict called: ridership_date
ridership_date = OrderedDict()

# Iterate over the entries
for date, riders in entries:
    # If a key does not exist in ridership_date, set it to 0
    if date not in ridership_date:
        ridership_date[date] = 0

    # Add riders to the date key in ridership_date
    ridership_date[date] += riders

# Print the first 31 records
print(list(ridership_date.items())[:31])


# 7

# Print the first key in ridership_date
print(list(ridership_date.keys())[0])

# Pop the first item from ridership_date and print it
print(ridership_date.popitem(last=False))

# Print the last key in ridership_date
print(list(ridership_date.keys())[-1])

# Pop the last item from ridership_date and print it
print(ridership_date.popitem())


# 8

# Create the namedtuple: DateDetails
DateDetails = namedtuple('DateDetails', ['date', 'stop', 'riders'])

# Create the empty list: labeled_entries
labeled_entries = []

# Iterate over the entries list
for date, stop, riders in entries:
    # Append a new DateDetails namedtuple instance for each entry to labeled_entries
    labeled_entries.append(DateDetails(date, stop, riders))

# Print the first 5 items in labeled_entries
print(labeled_entries[:5])


# 9

# Iterate over the first twenty items in labeled_entries
for item in labeled_entries[:20]:
    # Print each item's stop
    print(item.stop)

    # Print each item's date
    print(item.date)

    # Print each item's riders
    print(item.riders)
