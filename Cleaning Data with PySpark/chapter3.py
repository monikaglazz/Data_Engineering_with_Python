from pyspark.sql.functions import broadcast
from pyspark.sql import SparkSession
from datetime import time
from pyspark.sql.types import StringType, StructType, StructField

spark = SparkSession.builder.getOrCreate()


# ex 1 "Caching a DataFrame"
departures_df = spark.read.csv('AA_DFW_2015_Departures_Short.csv')

start_time = time.time()

# Add caching to the unique rows in departures_df
departures_df = departures_df.distinct().cache()

# Count the unique rows in departures_df, noting how long the operation takes
print("Counting %d rows took %f seconds" %
      (departures_df.count(), time.time() - start_time))

# Count the rows again, noting the variance in time of a cached DataFrame
start_time = time.time()
print("Counting %d rows again took %f seconds" %
      (departures_df.count(), time.time() - start_time))


# ex 2 "Removing a DataFrame from cache"
# Determine if departures_df is in the cache
print("Is departures_df cached?: %s" % departures_df.is_cached)
print("Removing departures_df from cache")

# Remove departures_df from the cache
departures_df.unpersist()

# Check the cache status again
print("Is departures_df cached?: %s" % departures_df.is_cached)


# ex 3 "File import performance"
# Import the full and split files into DataFrames
full_df = spark.read.csv('departures_full.txt.gz')
split_df = spark.read.csv('departures_*.txt.gz')

# Print the count and run time for each DataFrame
start_time_a = time.time()
print("Total rows in full DataFrame:\t%d" % full_df.count())
print("Time to run: %f" % (time.time() - start_time_a))

start_time_b = time.time()
print("Total rows in split DataFrame:\t%d" % split_df.count())
print("Time to run: %f" % (time.time() - start_time_b))


# ex 4 "Reading Spark configurations"
# Name of the Spark application instance
app_name = spark.conf.get('spark.app.name')

# Driver TCP port
driver_tcp_port = spark.conf.get('spark.driver.port')

# Number of join partitions
num_partitions = spark.conf.get('spark.sql.shuffle.partitions')

# Show the results
print("Name: %s" % app_name)
print("Driver TCP port: %s" % driver_tcp_port)
print("Number of partitions: %s" % num_partitions)


# ex 5 "Writing Spark configurations"
# Store the number of partitions in variable
before = departures_df.rdd.getNumPartitions()

# Configure Spark to use 500 partitions
spark.conf.set('spark.sql.shuffle.partitions', 500)

# Recreate the DataFrame using the departures data file
departures_df = spark.read.csv('departures.txt.gz').distinct()

# Print the number of partitions for each instance
print("Partition count before change: %d" % before)
print("Partition count after change: %d" %
      departures_df.rdd.getNumPartitions())


# ex 6 "Normal joins"
fl_list = [['01/01/2018', '0005', 'HNL', '498'], ['01/01/2018', '0007', 'OGG', '501'], ['01/01/2018', '0043', 'DTW', '0'], ['01/01/2018', '0051', 'STL', '100'], ['01/01/2018', '0075', 'DCA', '147'], ['01/01/2018', '0096', 'STL', '92'], ['01/01/2018', '0103', 'SJC', '227'], ['01/01/2018', '0119', 'OGG', '517'], ['01/01/2018', '0123', 'HNL', '489'], ['01/01/2018', '0128', 'MCO', '141'],
           ['01/01/2018', '0132', 'EWR', '201'], ['01/01/2018', '0140', 'SJC', '215'], ['01/01/2018', '0174', 'RDU', '140'], ['01/01/2018', '0190', 'SAT', '68'], ['01/01/2018', '0200', 'SFO', '215'], ['01/01/2018', '0209', 'MIA', '169'], ['01/01/2018', '0217', 'LAS', '178'], ['01/01/2018', '0229', 'KOA', '534'], ['01/01/2018', '0244', 'CVG', '115'], ['01/01/2018', '0262', 'MIA', '159']]

schema_fl = StructType([
    StructField("Date_(MM/DD/YYYY)", StringType(), False),
    StructField("Flight_Number", StringType(), False),
    StructField("Destination_Airport", StringType(), False),
    StructField("Actual_elapsed time_(Minutes)", StringType(), False)
])

# Creating a DataFrame from the list of data and the schema
flights_df = spark.createDataFrame(fl_list, schema_fl)

ar_list = [['Goroka Airport', 'GKA'], ['Madang Airport', 'MAG'], ['Mount Hagen Kagamuga Airport', 'HGU'], ['Nadzab Airport', 'LAE'], ['Port Moresby Jacksons International Airport', 'POM'], ['Wewak International Airport', 'WWK'], ['Narsarsuaq Airport', 'UAK'], ['Godthaab / Nuuk Airport', 'GOH'], ['Kangerlussuaq Airport', 'SFJ'], ['Thule Air Base',
                                                                                                                                                                                                                                                                                                                                           'THU'], ['Akureyri Airport', 'AEY'], ['Egilsstaðir Airport', 'EGS'], ['Hornafjörður Airport', 'HFN'], ['Húsavík Airport', 'HZK'], ['Ísafjörður Airport', 'IFJ'], ['Keflavik International Airport', 'KEF'], ['Patreksfjörður Airport', 'PFJ'], ['Reykjavik Airport', 'RKV'], ['Siglufjörður Airport', 'SIJ'], ['Vestmannaeyjar Airport', 'VEY']]
schema_ar = StructType([
    StructField("AIRPORTNAME", StringType(), False),
    StructField("IATA", StringType(), False),
])

# Creating a DataFrame from the list of data and the schema
airports_df = spark.createDataFrame(ar_list, schema_ar)


# Join the flights_df and aiports_df DataFrames
normal_df = flights_df.join(
    airports_df, flights_df.Destination_Airport == airports_df.IATA)

# Show the query plan
normal_df.explain()


# ex 7 "Using broadcasting on Spark joins"
# Join the flights_df and airports_df DataFrames using broadcasting
broadcast_df = flights_df.join(broadcast(airports_df),
                               flights_df.Destination_Airport == airports_df.IATA)

# Show the query plan and compare against the original
broadcast_df.explain()


# ex 8 "Comparing broadcast vs normal joins"
start_time = time.time()
# Count the number of rows in the normal DataFrame
normal_count = normal_df.count()
normal_duration = time.time() - start_time

start_time = time.time()
# Count the number of rows in the broadcast DataFrame
broadcast_count = broadcast_df.count()
broadcast_duration = time.time() - start_time

# Print the counts and the duration of the tests
print("Normal count:\t\t%d\tduration: %f" %
      (normal_count, normal_duration))
print("Broadcast count:\t%d\tduration: %f" %
      (broadcast_count, broadcast_duration))
