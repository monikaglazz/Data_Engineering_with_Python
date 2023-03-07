from pyspark.sql import SparkSession


spark = SparkSession.builder.getOrCreate()
file_path = "/Data_Engineering_with_Python/Introduction to PySpark/flights.csv"
table = airports = spark.read.csv(file_path, header=True)
table.write.mode("overwrite").saveAsTable("flights")