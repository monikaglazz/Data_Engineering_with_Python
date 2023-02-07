import dask.dataframe as dd
import pandas as pd

# Complete the SELECT statement
data = pd.read_sql("""
SELECT first_name, last_name FROM "Customer"
ORDER BY last_name, first_name
""", db_engine)

# Show the first 3 rows of the DataFrame
print(data.head(3))

# Show the info of the DataFrame
print(data.info())

# Complete the SELECT statement
data = pd.read_sql("""
SELECT * FROM "Customer"
INNER JOIN "Order"
ON "Order"."customer_id"="Customer"."id"
""", db_engine)

# Show the id column of data
print(data.id)

# Function to apply a function over multiple cores


@print_timing
def parallel_apply(apply_func, groups, nb_cores):
    with Pool(nb_cores) as p:
        results = p.map(apply_func, groups)
    return pd.concat(results)

# take_mean_age() calculates the average athlete's age in a given year in the Olympics events dataset.
# athlete_events contains amongst others, two columns:
# Year: the year the Olympic event took place
# Age: the age of the Olympian


# Parallel apply using 1 core
parallel_apply(take_mean_age, athlete_events.groupby('Year'), 1)

# Parallel apply using 2 cores
parallel_apply(take_mean_age, athlete_events.groupby('Year'), 2)

# Parallel apply using 4 cores
parallel_apply(take_mean_age, athlete_events.groupby('Year'), 4)


# Set the number of partitions
athlete_events_dask = dd.from_pandas(athlete_events, npartitions=4)


# Print the type of athlete_events_spark
print(type(athlete_events_spark))

# Print the schema of athlete_events_spark
print(athlete_events_spark.printSchema())

# Group by the Year, and find the mean Age
print(athlete_events_spark.groupBy('Year').mean('Age'))

# Group by the Year, and find the mean Age
print(athlete_events_spark.groupBy('Year').mean('Age').show())


# Create the DAG object
dag = DAG(dag_id="car_factory_simulation",
          default_args={"owner": "airflow",
                        "start_date": airflow.utils.dates.days_ago(2)},
          schedule_interval="0 * * * *")
