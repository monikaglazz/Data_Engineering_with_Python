from pyspark.sql import SparkSession
from spark_session import spark
import pandas as pd
import numpy as np


# ex 1 "Create SparkSession"
my_spark = SparkSession.builder.getOrCreate()

print(my_spark)


# ex 2 "Viewing tables"
# Print the tables in the catalog
print(spark.catalog.listTables())


# ex 3 "Get data with sql and spark"
query = "FROM flights SELECT * LIMIT 10"

flights10 = spark.sql(query)

# Show the results
flights10.show()


# ex 4 "Spark DataFrame to Pandas"
query = "SELECT origin, dest, COUNT(*) as N FROM flights GROUP BY origin, dest"

flight_counts = spark.sql(query)

# Convert the results to a pandas DataFrame
pd_counts = flight_counts.toPandas()

print(pd_counts.head())


# ex 5 "Put some Spark in your data"
# create a pandas DataFrame of random numbers
pd_temp = pd.DataFrame(np.random.random(10))

# Create spark_temp from pd_temp
spark_temp = spark.createDataFrame(pd_temp)

# Examine the tables in the catalog
print(spark.catalog.listTables())

# Add spark_temp to the catalog
spark_temp.createOrReplaceTempView("temp")

# Examine the tables in the catalog again
print(spark.catalog.listTables())


# ex 6 "Read file into Spark"
file_path = "/Data_Engineering_with_Python/Introduction to PySpark/airports.csv"

# Read in the airports data
airports = spark.read.csv(file_path, header=True)

airports.show()
