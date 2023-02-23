import dask.dataframe as dd
import pandas as pd
from flask_sqlalchemy import SQLAlchemy as sqlalchemy
from multiprocessing import Pool
import numpy as np
from pyspark.sql import SparkSession

# 1

connection_uri = "postgresql://repl:password@localhost:5432/pagila"
db_engine = sqlalchemy.create_engine(connection_uri)

# Complete the SELECT statement
data = pd.read_sql("""
SELECT first_name, last_name FROM "Customer"
ORDER BY last_name, first_name
""", db_engine)

# Show the first 3 rows of the DataFrame
print(data.head(3))

# Show the info of the DataFrame
print(data.info())


# 2

# Complete the SELECT statement
data = pd.read_sql("""
SELECT * FROM "Customer"
INNER JOIN "Order"
ON "Order"."customer_id"="Customer"."id"
""", db_engine)

# Show the id column of data
print(data.id)


# 3

# Function to apply a function over multiple cores
@print_timing
def parallel_apply(apply_func, groups, nb_cores):
    with Pool(nb_cores) as p:
        results = p.map(apply_func, groups)
    return pd.concat(results)


# Average athlete's age in a given year in the Olympics events dataset.
def take_mean_age(year_and_group):
    year, group = year_and_group
    return pd.DataFrame({"Age": group["Age"].mean()}, index=[year])


athlete = np.array([
    [1, "A Dijiang", "M", 24.0, 1992],
    [2, "A Lamusi", "M",  23.0, 2012],
    [3, "Gunnar Nielsen Aaby", "M",  24.0, 1920],
    [4, "Edgar Lindenau Aabye",  "M",  34.0, 1900],
    [5, "Christine Jacoba Aaftink",   "F", 21.0, 1988],
    [5, "Christine Jacoba Aaftink",   "F",  21.0, 1988],
    [5, "Christine Jacoba Aaftink",  "F",  25.0, 1992],
    [5, "Christine Jacoba Aaftink", "F",  25.0,  1992],
    [5, "Christine Jacoba Aaftink", "F",  27.0, 1994],
    [5, "Christine Jacoba Aaftink", "F",  27.0, 1994],
    [6, "Per Knut Aaland",   "M",  31.0,  1992],
    [6, "Per Knut Aaland",   "M",  31.0, 1992],
    [6, "Per Knut Aaland",   "M",  31.0, 1992],
    [6, "Per Knut Aaland",   "M",  31.0, 1992],
    [6, "Per Knut Aaland",   "M", 33.0, 1994],
    [6, "Per Knut Aaland",   "M",   33.0,  1994],
    [6, "Per Knut Aaland",   "M",  33.0, 1994],
    [6, "Per Knut Aaland",   "M",  33.0, 1994],
    [7, "John Aalberg",   "M",  31.0, 1992],
    [7, "John Aalberg",   "M",  31.0,  1992],
    [7, "John Aalberg",   "M",  31.0, 1992],
    [7, "John Aalberg",   "M",  31.0, 1992],
    [7, "John Aalberg",   "M",  33.0, 1994],
    [7, "John Aalberg",   "M",  33.0, 1994],
    [7, "John Aalberg",   "M",  33.0, 1994]
])


athlete_events = pd.DataFrame(athlete,
                              columns=['ID', 'Name', 'Sex', 'Age', 'Year'])
athlete_events = athlete_events.set_index('ID')

# Parallel apply using 1 core
parallel_apply(take_mean_age, athlete_events.groupby('Year'), 1)

# Parallel apply using 2 cores
parallel_apply(take_mean_age, athlete_events.groupby('Year'), 2)

# Parallel apply using 4 cores
parallel_apply(take_mean_age, athlete_events.groupby('Year'), 4)


# 4

# Set the number of partitions
athlete_events_dask = dd.from_pandas(athlete_events, npartitions=4)

# create pyspark dataframe from pandas data frame
spark = SparkSession.builder.appName("PandasToPySpark").getOrCreate()
athlete_events_spark = spark.createDataFrame(athlete_events)

(athlete_events_spark.groupBy('Year').mean('Age').show())
# Print the type of athlete_events_spark
print(type(athlete_events_spark))


# 5

# Print the schema of athlete_events_spark
print(athlete_events_spark.printSchema())

# Group by the Year, and find the mean Age
print(athlete_events_spark.groupBy('Year').mean('Age'))

# Group by the Year, and find the mean Age
print(athlete_events_spark.groupBy('Year').mean('Age').show())


# 6

# Create the DAG object
dag = DAG(dag_id="car_factory_simulation",
          default_args={"owner": "airflow",
                        "start_date": airflow.utils.dates.days_ago(2)},
          schedule_interval="0 * * * *")
