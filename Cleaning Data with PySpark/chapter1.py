from pyspark.sql.types import *
from pyspark.sql import SparkSession
import pyspark.sql.functions as F

spark = SparkSession.builder.getOrCreate()

# ex 1 "Defining a schema"
# Define a new schema using the StructType method
people_schema = StructType([
    # Define a StructField for each field
    StructField('name', StringType(), False),
    StructField('age', IntegerType(), False),
    StructField('city', StringType(), False)
])


# ex 2 "Using lazy processing"
# Load the CSV file
aa_dfw_df = spark.read.format('csv').options(
    Header=True).load('AA_DFW_2017.csv')

# Add the airport column using the F.lower() method
aa_dfw_df = aa_dfw_df.withColumn(
    'airport', F.lower(aa_dfw_df['Destination Airport']))

# Drop the Destination Airport column
aa_dfw_df = aa_dfw_df.drop(aa_dfw_df['Destination Airport'])

# Show the DataFrame
aa_dfw_df.show()


# ex 3 "Saving a DataFrame in Parquet format"
df1 = a_dfw_df = spark.read.format('csv').options(
    Header=True).load('AA_DFW_2014.csv')
df2 = a_dfw_df = spark.read.format('csv').options(
    Header=True).load('AA_DFW_2015.csv')

# View the row count of df1 and df2
print("df1 Count: %d" % df1.count())
print("df2 Count: %d" % df2.count())

# Combine the DataFrames into one
df3 = df1.union(df2)

# Save the df3 DataFrame in Parquet format
df3.write.parquet('AA_DFW_ALL.parquet', mode='overwrite')

# Read the Parquet file into a new DataFrame and run a count
print(spark.read.parquet('AA_DFW_ALL.parquet').count())


# ex 4 "SQL and Parquet"
# Read the Parquet file into flights_df
flights_df = spark.read.parquet('AA_DFW_ALL.parquet')

# Register the temp table
flights_df.createOrReplaceTempView('flights')

# Run a SQL query of the average flight duration
avg_duration = spark.sql(
    'SELECT avg(flight_duration) from flights').collect()[0]
print('The average flight time is: %d' % avg_duration)
