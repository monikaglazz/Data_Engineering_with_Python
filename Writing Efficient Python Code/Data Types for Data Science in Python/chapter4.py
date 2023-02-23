# Import the datetime object from datetime
from datetime import datetime, timedelta
from collections import defaultdict
from pytz import timezone
import pendulum

# 1

dates_list = ['02/19/2001', '04/10/2001', '05/30/2001', '07/19/2001', '09/07/2001', '10/27/2001', '12/16/2001', '02/04/2002', '03/26/2002', '05/15/2002', '07/04/2002', '08/23/2002', '10/12/2002', '12/01/2002', '01/20/2003', '03/11/2003', '04/30/2003', '06/19/2003', '08/08/2003', '09/27/2003', '11/16/2003', '01/05/2004', '02/24/2004', '04/14/2004', '06/03/2004', '07/23/2004', '09/11/2004', '10/31/2004', '12/20/2004', '02/08/2005', '03/30/2005', '05/19/2005', '07/08/2005', '08/27/2005', '10/16/2005', '12/05/2005', '01/24/2006', '03/15/2006', '05/04/2006', '06/23/2006', '08/12/2006', '10/01/2006', '11/20/2006', '01/09/2007', '02/28/2007', '04/19/2007', '06/08/2007', '07/28/2007', '09/16/2007', '11/05/2007', '12/25/2007', '02/13/2008', '04/03/2008', '05/23/2008', '07/12/2008', '08/31/2008', '10/20/2008', '12/09/2008', '01/28/2009', '03/19/2009', '05/08/2009', '06/27/2009', '08/16/2009', '10/05/2009', '11/24/2009', '01/13/2010', '03/04/2010', '04/23/2010', '06/12/2010', '08/01/2010', '09/20/2010', '11/09/2010', '12/29/2010', '02/17/2011', '04/08/2011', '05/28/2011', '07/17/2011', '09/05/2011', '10/24/2011', '11/12/2011', '01/01/2012', '02/20/2012', '04/10/2012', '05/30/2012', '07/19/2012', '09/07/2012', '10/27/2012', '12/16/2012', '02/04/2013', '03/26/2013', '05/15/2013', '07/04/2013', '08/23/2013', '10/12/2013', '12/01/2013', '01/20/2014', '03/11/2014', '04/30/2014', '06/19/2014', '08/08/2014', '09/27/2014', '11/16/2014', '07/05/2014', '01/24/2015', '03/15/2015', '05/04/2015', '06/23/2015', '08/12/2015', '10/01/2015', '11/20/2015', '01/09/2016', '02/28/2016', '04/18/2016', '06/07/2016', '07/27/2016', '09/15/2016', '11/04/2016']


# Iterate over the dates_list 
for date_str in dates_list:
    # Convert each date to a datetime object: date_dt
    date_dt = datetime.strptime(date_str, '%m/%d/%Y')
    
    # Print each date_dt
    print(date_dt)



# 2

# Loop over the first 10 items of the datetimes_list
for item in dates_list[:10]:
    # Print out the record as a string in the format of 'MM/DD/YYYY'
    print(item.strftime('%m/%d/%Y'))
    
    # Print out the record as an ISO standard string
    print(item.isoformat())


# 3

daily_summaries = [('01/01/2001', 'U', '297192', '126455', '423647'), ('01/02/2001', 'W', '780827', '501952', '1282779'), ('01/03/2001', 'W', '824923', '536432', '1361355'), ('01/04/2001', 'W', '870021', '550011', '1420032'), ('01/05/2001', 'W', '890426', '557917', '1448343'), ('01/06/2001', 'A', '577401', '255356', '832757'), ('01/07/2001', 'U', '375831', '169825', '545656'), ('01/08/2001', 'W', '985221', '590706', '1575927'), ('01/09/2001', 'W', '978377', '599905', '1578282'), ('01/10/2001', 'W', '984884', '602052', '1586936'), ('01/11/2001', 'W', '995561', '607503', '1603064'), ('01/12/2001', 'W', '1018985', '605252', '1624237'), ('01/13/2001', 'A', '591791', '270056', '861847'), ('01/14/2001', 'U', '373091', '174842', '547933'), ('01/15/2001', 'W', '675845', '412149', '1087994'), ('01/16/2001', 'W', '1024367', '622163', '1646530'), ('01/17/2001', 'W', '1018690', '620343', '1639033'), ('01/18/2001', 'W', '1006996', '618832', '1625828'), ('01/19/2001', 'W', '909964', '583851', '1493815'), ('01/20/2001', 'A', '582348', '263815', '846163'), ('01/21/2001', 'U', '378381', '172107', '550488'), ('01/22/2001', 'W', '1005936', '598777', '1604713'), ('01/23/2001', 'W', '1019983', '610352', '1630335'), ('01/24/2001', 'W', '991661', '606835', '1598496'), ('01/25/2001', 'W', '1004257', '609877', '1614134'), ('01/26/2001', 'W', '965324', '597039', '1562363'), ('01/27/2001', 'A', '590836', '268078', '858914'), ('01/28/2001', 'U', '368819', '174434', '543253'), ('01/29/2001', 'W', '953532', '587052', '1540584'), ('01/30/2001', 'W', '982046', '607858', '1589904'), ('01/31/2001', 'W', '999392', '610508', '1609900'), ('02/01/2001', 'W', '1054608', '615268', '1669876'), ('02/02/2001', 'W', '966701', '577767', '1544468'), ('02/03/2001', 'A', '611703', '263612', '875315'), ('02/04/2001', 'U', '404212', '178398', '582610'), ('02/05/2001', 'W', '1045944', '600588', '1646532'), ('02/06/2001', 'W', '1039393', '612435', '1651828'), ('02/07/2001', 'W', '1015059', '609022', '1624081'), ('02/08/2001', 'W', '1007760', '610237', '1617997'), ('02/09/2001', 'W', '970826', '593354', '1564180'), ('02/10/2001', 'A', '605404', '271313', '876717'), ('02/11/2001', 'U', '405433', '178810', '584243'), ('02/12/2001', 'W', '872330', '539393', '1411723'), ('02/13/2001', 'W', '1050834', '622753', '1673587'), ('02/14/2001', 'W', '1004304', '610966', '1615270'), ('02/15/2001', 'W', '1028938', '613323', '1642261'), ('02/16/2001', 'W', '1033040', '601418', '1634458'), ('02/17/2001', 'A', '591717', '269294', '861011'), ('02/18/2001', 'U', '388788', '176855', '565643'), ('02/19/2001', 'W', '782447', '457891', '1240338'), ('02/20/2001', 'W', '1035400', '610284', '1645684'), ('02/21/2001', 'W', '986212', '600133', '1586345'), ('02/22/2001', 'W', '986399', '606302', '1592701'), ('02/23/2001', 'W', '1024235', '602352', '1626587'), ('02/24/2001', 'A', '505193', '246795', '751988'), ('02/25/2001', 'U', '351637', '172132', '523769'), ('02/26/2001', 'W', '1009329', '609256', '1618585'), ('02/27/2001', 'W', '1000630', '609305', '1609935'), ('02/28/2001', 'W', '990416', '610013', '1600429'), ('03/01/2001', 'W', '1051889', '618440', '1670329'), ('03/02/2001', 'W', '1062234', '611578', '1673812'), ('03/03/2001', 'A', '678870', '286786', '965656'), ('03/04/2001', 'U', '385978', '178292', '564270'), ('03/05/2001', 'W', '863086', '549759', '1412845'), ('03/06/2001', 'W', '1013530', '603561', '1617091'), ('03/07/2001', 'W', '1028462', '616666', '1645128'), ('03/08/2001', 'W', '1000946', '611371', '1612317'), ('03/09/2001', 'W', '1038368', '606672', '1645040'), ('03/10/2001', 'A', '633472', '283251', '916723'), ('03/11/2001', 'U', '410081', '188228', '598309'), ('03/12/2001', 'W', '979411', '588857', '1568268'), ('03/13/2001', 'W', '1017685', '611347', '1629032'), ('03/14/2001', 'W', '1025283', '619417', '1644700'), ('03/15/2001', 'W', '960667', '596612', '1557279'), ('03/16/2001', 'W', '923613', '583359', '1506972'), ('03/17/2001', 'A', '602158', '343893', '946051'), ('03/18/2001', 'U', '412146', '194257', '606403'), ('03/19/2001', 'W', '1021700', '602469', '1624169'), ('03/20/2001', 'W', '1034388', '618340', '1652728'), ('03/21/2001', 'W', '1029332', '616764', '1646096'), ('03/22/2001', 'W', '1030741', '617815', '1648556'), ('03/23/2001', 'W', '1030685', '605605', '1636290'), ('03/24/2001', 'A', '604139', '277028', '881167'), ('03/25/2001', 'U', '348817', '170742', '519559'), ('03/26/2001', 'W', '989316', '583176', '1572492'), ('03/27/2001', 'W', '1017904', '600914', '1618818'), ('03/28/2001', 'W', '1007699', '601999', '1609698'), ('03/29/2001', 'W', '1020098', '605027', '1625125'), ('03/30/2001', 'W', '978244', '590403', '1568647'), ('03/31/2001', 'A', '626223', '280950', '907173'), ('04/01/2001', 'U', '417716', '192717', '610433'), ('04/02/2001', 'W', '1023629', '611098', '1634727'), ('04/03/2001', 'W', '1057275', '613993', '1671268'), ('04/04/2001', 'W', '1047634', '625348', '1672982'), ('04/05/2001', 'W', '973118', '606535', '1579653'), ('04/06/2001', 'W', '1015046', '611352', '1626398'), ('04/07/2001', 'A', '642265', '297971', '940236'), ('04/08/2001', 'U', '437035', '200720', '637755'), ('04/09/2001', 'W', '998290', '596418', '1594708'), ('04/10/2001', 'W', '1024817', '613311', '1638128'), ('04/11/2001', 'W', '985906', '606764', '1592670'), ('04/12/2001', 'W', '991795', '608691', '1600486'), ('04/13/2001', 'W', '865706', '527116', '1392822'), ('04/14/2001', 'A', '628526', '279728', '908254'), ('04/15/2001', 'U', '364972', '163191', '528163'), ('04/16/2001', 'W', '859713', '564614', '1424327'), ('04/17/2001', 'W', '877834', '583859', '1461693'), ('04/18/2001', 'W', '907539', '599600', '1507139'), ('04/19/2001', 'W', '917518', '596505', '1514023'), ('04/20/2001', 'W', '922082', '590659', '1512741'), ('04/21/2001', 'A', '603039', '293701', '896740'), ('04/22/2001', 'U', '384255', '185526', '569781'), ('04/23/2001', 'W', '979788', '590446', '1570234'), ('04/24/2001', 'W', '1031150', '618513', '1649663'), ('04/25/2001', 'W', '977794', '609447', '1587241'), ('04/26/2001', 'W', '1028140', '624617', '1652757'), ('04/27/2001', 'W', '1034472', '610723', '1645195'), ('04/28/2001', 'A', '624970', '289747', '914717'), ('04/29/2001', 'U', '423377', '200002', '623379'), ('04/30/2001', 'W', '1008390', '600424', '1608814'), ('05/01/2001', 'W', '1067496', '632996', '1700492')]

# Create a defaultdict of an integer: monthly_total_rides
monthly_total_rides = defaultdict(int)

# Loop over the list daily_summaries
for daily_summary in daily_summaries:
    # Convert the service_date to a datetime object
    service_datetime = datetime.strptime(daily_summary[0], '%m/%d/%Y')

    # Add the total rides to the current amount for the month
    monthly_total_rides[service_datetime.month] += int(daily_summary[4])
    
# Print monthly_total_rides
print(monthly_total_rides)


# 4

# Compute the local datetime: local_dt
local_dt = datetime.now()

# Print the local datetime
print(local_dt)

# Compute the UTC datetime: utc_dt
utc_dt = datetime.utcnow()

# Print the UTC datetime
print(utc_dt)

# 5

# Create a Timezone object for Chicago
chicago_usa_tz = timezone('US/Central')

# Create a Timezone object for New York
ny_usa_tz = timezone('US/Eastern')

# Iterate over the daily_summaries list
for orig_dt, ridership in daily_summaries:

    # Make the orig_dt timezone "aware" for Chicago
    chicago_dt = orig_dt.replace(tzinfo=chicago_usa_tz)
    
    # Convert chicago_dt to the New York Timezone
    ny_dt = chicago_dt.astimezone(ny_usa_tz)
    
    # Print the chicago_dt, ny_dt, and ridership
    print('Chicago: %s, NY: %s, Ridership: %s' % (chicago_dt, ny_dt, ridership))


# 6

review_dates = [datetime.datetime(2013, 12, 22, 0, 0), datetime.datetime(2013, 12, 23, 0, 0), datetime.datetime(2013, 12, 24, 0, 0), datetime.datetime(2013, 12, 25, 0, 0), datetime.datetime(2013, 12, 26, 0, 0), datetime.datetime(2013, 12, 27, 0, 0), datetime.datetime(2013, 12, 28, 0, 0), datetime.datetime(2013, 12, 29, 0, 0), datetime.datetime(2013, 12, 30, 0, 0), datetime.datetime(2013, 12, 31, 0, 0)]


# Build a timedelta of 30 days: glanceback
glanceback = timedelta(days = 30)

# Iterate over the review_dates as date
for date in review_dates:
    # Calculate the date 30 days back: prior_period_dt
    prior_period_dt = date - glanceback
    
    # Print the review_date, day_type and total_ridership
    print('Date: %s, Type: %s, Total Ridership: %s' %
         (date, 
          daily_summaries[date]['day_type'], 
          daily_summaries[date]['total_ridership']))

    # Print the prior_period_dt, day_type and total_ridership
    print('Date: %s, Type: %s, Total Ridership: %s' %
         (prior_period_dt,
          daily_summaries[prior_period_dt]['day_type'], 
          daily_summaries[prior_period_dt]['total_ridership']))


# 7

date_ranges = [(datetime.datetime(2001, 1, 30, 0, 0), datetime.datetime(2001, 3, 1, 0, 0)),
(datetime.datetime(2001, 3, 31, 0, 0), datetime.datetime(2001, 4, 30, 0, 0)),
(datetime.datetime(2001, 5, 30, 0, 0), datetime.datetime(2001, 6, 29, 0, 0)),
(datetime.datetime(2001, 7, 29, 0, 0), datetime.datetime(2001, 8, 28, 0, 0)),
(datetime.datetime(2001, 9, 27, 0, 0), datetime.datetime(2001, 10, 27, 0, 0)),
(datetime.datetime(2001, 11, 26, 0, 0), datetime.datetime(2001, 12, 26, 0, 0)),
(datetime.datetime(2002, 1, 25, 0, 0), datetime.datetime(2002, 2, 24, 0, 0)),
(datetime.datetime(2002, 3, 26, 0, 0), datetime.datetime(2002, 4, 25, 0, 0)),
(datetime.datetime(2002, 5, 25, 0, 0), datetime.datetime(2002, 6, 24, 0, 0)),
(datetime.datetime(2002, 7, 24, 0, 0), datetime.datetime(2002, 8, 23, 0, 0)),
(datetime.datetime(2002, 9, 22, 0, 0), datetime.datetime(2002, 10, 22, 0, 0)),
(datetime.datetime(2002, 11, 21, 0, 0), datetime.datetime(2002, 12, 21, 0, 0)),
(datetime.datetime(2003, 1, 20, 0, 0), datetime.datetime(2003, 2, 19, 0, 0)),
(datetime.datetime(2003, 3, 21, 0, 0), datetime.datetime(2003, 4, 20, 0, 0)),
(datetime.datetime(2003, 5, 20, 0, 0), datetime.datetime(2003, 6, 19, 0, 0)),
(datetime.datetime(2003, 7, 19, 0, 0), datetime.datetime(2003, 8, 18, 0, 0)),
(datetime.datetime(2003, 9, 17, 0, 0), datetime.datetime(2003, 10, 17, 0, 0)),
(datetime.datetime(2003, 11, 16, 0, 0), datetime.datetime(2003, 12, 16, 0, 0)),
(datetime.datetime(2004, 1, 15, 0, 0), datetime.datetime(2004, 2, 14, 0, 0)),
(datetime.datetime(2004, 3, 15, 0, 0), datetime.datetime(2004, 4, 14, 0, 0)),
(datetime.datetime(2004, 5, 14, 0, 0), datetime.datetime(2004, 6, 13, 0, 0)),
(datetime.datetime(2004, 7, 13, 0, 0), datetime.datetime(2004, 8, 12, 0, 0)),
(datetime.datetime(2004, 9, 11, 0, 0), datetime.datetime(2004, 10, 11, 0, 0)),
(datetime.datetime(2004, 11, 10, 0, 0), datetime.datetime(2004, 12, 10, 0, 0)),
(datetime.datetime(2005, 1, 9, 0, 0), datetime.datetime(2005, 2, 8, 0, 0)),
(datetime.datetime(2005, 3, 10, 0, 0), datetime.datetime(2005, 4, 9, 0, 0)),
(datetime.datetime(2005, 5, 9, 0, 0), datetime.datetime(2005, 6, 8, 0, 0)),
(datetime.datetime(2005, 7, 8, 0, 0), datetime.datetime(2005, 8, 7, 0, 0)),
(datetime.datetime(2005, 9, 6, 0, 0), datetime.datetime(2005, 10, 6, 0, 0)),
(datetime.datetime(2005, 11, 5, 0, 0), datetime.datetime(2005, 12, 5, 0, 0)),
(datetime.datetime(2006, 1, 4, 0, 0), datetime.datetime(2006, 2, 3, 0, 0)),
(datetime.datetime(2006, 3, 5, 0, 0), datetime.datetime(2006, 4, 4, 0, 0)),
(datetime.datetime(2006, 5, 4, 0, 0), datetime.datetime(2006, 6, 3, 0, 0)),
(datetime.datetime(2006, 7, 3, 0, 0), datetime.datetime(2006, 8, 2, 0, 0)),
(datetime.datetime(2006, 9, 1, 0, 0), datetime.datetime(2006, 10, 1, 0, 0)),
(datetime.datetime(2006, 10, 31, 0, 0), datetime.datetime(2006, 11, 30, 0, 0)),
(datetime.datetime(2006, 12, 30, 0, 0), datetime.datetime(2007, 1, 29, 0, 0)),
(datetime.datetime(2007, 2, 28, 0, 0), datetime.datetime(2007, 3, 30, 0, 0)),
(datetime.datetime(2007, 4, 29, 0, 0), datetime.datetime(2007, 5, 29, 0, 0)),
(datetime.datetime(2007, 6, 28, 0, 0), datetime.datetime(2007, 7, 28, 0, 0)),
(datetime.datetime(2007, 8, 27, 0, 0), datetime.datetime(2007, 9, 26, 0, 0)),
(datetime.datetime(2007, 10, 26, 0, 0), datetime.datetime(2007, 11, 25, 0, 0)),
(datetime.datetime(2007, 12, 25, 0, 0), datetime.datetime(2008, 1, 24, 0, 0)),
(datetime.datetime(2008, 2, 23, 0, 0), datetime.datetime(2008, 3, 24, 0, 0)),
(datetime.datetime(2008, 4, 23, 0, 0), datetime.datetime(2008, 5, 23, 0, 0)),
(datetime.datetime(2008, 6, 22, 0, 0), datetime.datetime(2008, 7, 22, 0, 0)),
(datetime.datetime(2008, 8, 21, 0, 0), datetime.datetime(2008, 9, 20, 0, 0)),
(datetime.datetime(2008, 10, 20, 0, 0), datetime.datetime(2008, 11, 19, 0, 0)),
(datetime.datetime(2008, 12, 19, 0, 0), datetime.datetime(2009, 1, 18, 0, 0)),
(datetime.datetime(2009, 2, 17, 0, 0), datetime.datetime(2009, 3, 19, 0, 0)),
(datetime.datetime(2009, 4, 18, 0, 0), datetime.datetime(2009, 5, 18, 0, 0)),
(datetime.datetime(2009, 6, 17, 0, 0), datetime.datetime(2009, 7, 17, 0, 0)),
(datetime.datetime(2009, 8, 16, 0, 0), datetime.datetime(2009, 9, 15, 0, 0)),
(datetime.datetime(2009, 10, 15, 0, 0), datetime.datetime(2009, 11, 14, 0, 0)),
(datetime.datetime(2009, 12, 14, 0, 0), datetime.datetime(2010, 1, 13, 0, 0)),
(datetime.datetime(2010, 2, 12, 0, 0), datetime.datetime(2010, 3, 14, 0, 0)),
(datetime.datetime(2010, 4, 13, 0, 0), datetime.datetime(2010, 5, 13, 0, 0)),
(datetime.datetime(2010, 6, 12, 0, 0), datetime.datetime(2010, 7, 12, 0, 0)),
(datetime.datetime(2010, 8, 11, 0, 0), datetime.datetime(2010, 9, 10, 0, 0)),
(datetime.datetime(2010, 10, 10, 0, 0), datetime.datetime(2010, 11, 9, 0, 0)),
(datetime.datetime(2010, 12, 9, 0, 0), datetime.datetime(2011, 1, 8, 0, 0)),
(datetime.datetime(2011, 2, 7, 0, 0), datetime.datetime(2011, 3, 9, 0, 0)),
(datetime.datetime(2011, 4, 8, 0, 0), datetime.datetime(2011, 5, 8, 0, 0)),
(datetime.datetime(2011, 6, 7, 0, 0), datetime.datetime(2011, 7, 7, 0, 0)),
(datetime.datetime(2011, 8, 6, 0, 0), datetime.datetime(2011, 9, 5, 0, 0)),
(datetime.datetime(2011, 10, 5, 0, 0), datetime.datetime(2011, 10, 4, 0, 0)),
(datetime.datetime(2011, 11, 3, 0, 0), datetime.datetime(2011, 12, 3, 0, 0)),
(datetime.datetime(2012, 1, 2, 0, 0), datetime.datetime(2012, 2, 1, 0, 0)),
(datetime.datetime(2012, 3, 2, 0, 0), datetime.datetime(2012, 4, 1, 0, 0)),
(datetime.datetime(2012, 5, 1, 0, 0), datetime.datetime(2012, 5, 31, 0, 0)),
(datetime.datetime(2012, 6, 30, 0, 0), datetime.datetime(2012, 7, 30, 0, 0)),
(datetime.datetime(2012, 8, 29, 0, 0), datetime.datetime(2012, 9, 28, 0, 0)),
(datetime.datetime(2012, 10, 28, 0, 0), datetime.datetime(2012, 11, 27, 0, 0)),
(datetime.datetime(2012, 12, 27, 0, 0), datetime.datetime(2013, 1, 26, 0, 0)),
(datetime.datetime(2013, 2, 25, 0, 0), datetime.datetime(2013, 3, 27, 0, 0)),
(datetime.datetime(2013, 4, 26, 0, 0), datetime.datetime(2013, 5, 26, 0, 0)),
(datetime.datetime(2013, 6, 25, 0, 0), datetime.datetime(2013, 7, 25, 0, 0)),
(datetime.datetime(2013, 8, 24, 0, 0), datetime.datetime(2013, 9, 23, 0, 0)),
(datetime.datetime(2013, 10, 23, 0, 0), datetime.datetime(2013, 11, 22, 0, 0))]

# Iterate over the date_ranges
for start_date, end_date in date_ranges:
    # Print the End and Start Date
    print(end_date, start_date)
    # Print the difference between each end and start date
    print(end_date - start_date)



# 8

# Create a now datetime for Tokyo: tokyo_dt
tokyo_dt = pendulum.now(tz='Asia/Tokyo')

# Covert the tokyo_dt to Los Angeles: la_dt
la_dt = tokyo_dt.in_timezone('America/Los_Angeles')

# Print the ISO 8601 string of la_dt
print(la_dt.to_iso8601_string())


# 9

# Iterate over date_ranges
for start_date, end_date in date_ranges:

    # Convert the start_date string to a pendulum date: start_dt 
    start_dt = pendulum.parse(start_date, strict = False)
    
    # Convert the end_date string to a pendulum date: end_dt 
    end_dt = pendulum.parse(end_date, strict = False)
    
    # Print the End and Start Date
    print(end_dt, start_dt)
    
    # Calculate the difference between end_dt and start_dt: diff_period
    diff_period = end_dt - start_dt
    
    # Print the difference in days
    print(diff_period.in_days())
