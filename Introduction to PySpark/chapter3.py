from spark_session import planes, flights
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler
from pyspark.ml import Pipeline

# ex 1 "Join the DataFrames"
planes = planes.withColumnRenamed("year", "plane_year")

model_data = flights.join(planes, on="tailnum", how="leftouter")


# ex 2 "Cast the columns to integers"
model_data = model_data.withColumn(
    "arr_delay", model_data.arr_delay.cast("integer"))
model_data = model_data.withColumn(
    "air_time", model_data.air_time.cast("integer"))
model_data = model_data.withColumn("month", model_data.month.cast("integer"))
model_data = model_data.withColumn(
    "plane_year", model_data.plane_year.cast("integer"))


# ex 3 "Create the column plane_age"
model_data = model_data.withColumn(
    "plane_age", model_data.year - model_data.plane_year)


# ex 4 "Boolean column: is flight late or not?"
model_data = model_data.withColumn("is_late", model_data.arr_delay > 0)

model_data = model_data.withColumn("label", model_data.is_late.cast("integer"))

model_data = model_data.filter(
    "arr_delay is not NULL and dep_delay is not NULL and air_time is not NULL and plane_year is not NULL")


# ex 5 "Code carrier column"
carr_indexer = StringIndexer(inputCol="carrier", outputCol="carrier_index")

carr_encoder = OneHotEncoder(
    inputCol="carrier_index", outputCol="carrier_fact")


# ex 6 "Encode the dest column"
dest_indexer = StringIndexer(inputCol="dest", outputCol="dest_index")

dest_encoder = OneHotEncoder(inputCol="dest_index", outputCol="dest_fact")


#  ex 7 "Take columns and combine them into a new vector column"
vec_assembler = VectorAssembler(inputCols=[
                                "month", "air_time", "carrier_fact", "dest_fact", "plane_age"], outputCol="features")


# ex 8 "Make the Pipeline"
flights_pipe = Pipeline(
    stages=[dest_indexer, dest_encoder, carr_indexer, carr_encoder, vec_assembler])


# ex 9 "Fit and transform the data"
piped_data = flights_pipe.fit(model_data).transform(model_data)


#  ex 10 "Split the data into two pieces, training with 60% of the data, and test with 40% of the data"
training, test = piped_data.randomSplit([.6, .4])
