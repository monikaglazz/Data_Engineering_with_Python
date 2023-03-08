from pyspark.sql import SparkSession
from chapter1 import airports


spark = SparkSession.builder.getOrCreate()

# add table flights
file_path = "/Data_Engineering_with_Python/Introduction to PySpark/flights.csv"
flights = spark.read.csv(file_path, header=True)
flights.write.mode("overwrite").saveAsTable("flights")

# add table planes
file_path2 = "/Data_Engineering_with_Python/Introduction to PySpark/planes.csv"
planes = spark.read.csv(file_path2, header=True)
planes.write.mode("overwrite").saveAsTable("planes")

# add taable airports
airports.write.mode("overwrite").saveAsTable("airports")
