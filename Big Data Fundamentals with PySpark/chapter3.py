from pyspark import SparkContext
from pyspark.sql import SparkSession
import matplotlib.pyplot as plt

sc = SparkContext(appName="MyApp")
spark = SparkSession.builder.getOrCreate()

# ex 1 "RDD to DataFrame"
sample_list = [('Mona', 20), ('Jennifer', 34),
               ('John', 20), ('Jim', 26)]

# Create an RDD from the list
rdd = sc.parallelize(sample_list)

# Create a PySpark DataFrame
names_df = spark.createDataFrame(rdd, schema=['Name', 'Age'])

# Check the type of names_df
print("The type of names_df is", type(names_df))


# ex 2 "Loading CSV into DataFrame"
# Create an DataFrame from file_path
people_df = spark.read.csv("people.csv", header=True, inferSchema=True)

# Check the type of people_df
print("The type of people_df is", type(people_df))


# ex 3 "Inspecting data in PySpark DataFrame"
# Print the first 10 observations
people_df.show(10)

# Count the number of rows
print("There are {} rows in the people_df DataFrame.".format(people_df.count()))

# Count the number of columns and their names
print("There are {} columns in the people_df DataFrame and their names are {}".format(
    len(people_df.columns), people_df.columns))


# ex 4 "PySpark DataFrame subsetting and cleaning"
# Select name, sex and date of birth columns
people_df_sub = people_df.select('name', 'sex', 'date of birth')

# Print the first 10 observations from people_df_sub
people_df_sub.show(10)

# Remove duplicate entries from people_df_sub
people_df_sub_nodup = people_df_sub.dropDuplicates()

# Count the number of rows
print("There were {} rows before removing duplicates, and {} rows after removing duplicates".format(
    people_df_sub.count(), people_df_sub_nodup.count()))


# ex 5 "Running SQL Queries Programmatically"
# Create a temporary table "people"
people_df.createOrReplaceTempView("people")

# Construct a query to select the names of the people from the temporary table "people"
query = "SELECT name FROM people"

# Assign the result of Spark's query to people_df_names
people_df_names = spark.sql(query)

# Print the top 10 names of the people
people_df_names.show(10)


# ex 6 "SQL queries for filtering Table"
# Filter the people table to select female sex
people_female_df = spark.sql('SELECT * FROM people WHERE sex=="female"')

# Filter the people table DataFrame to select male sex
people_male_df = spark.sql('SELECT * FROM people WHERE sex=="male"')

# Count the number of rows in both DataFrames
print("There are {} rows in the people_female_df and {} rows in the people_male_df DataFrames".format(
    people_female_df.count(), people_male_df.count()))


# ex 7 "PySpark DataFrame visualization"
# Check the column names of names_df
print("The column names of names_df are", names_df.columns)

# Convert to Pandas DataFrame
df_pandas = names_df.toPandas()

# Create a horizontal bar plot
df_pandas.plot(kind='barh', x='Name', y='Age', colormap='winter_r')
plt.show()


# ex 8 "Practice"
# Load the Dataframe
fifa_df = spark.read.csv("Fifa2018_dataset.csv",
                         header=True, inferSchema=True)

# Check the schema of columns
fifa_df.printSchema()

# Show the first 10 observations
fifa_df.show(10)

# Print the total number of rows
print("There are {} rows in the fifa_df DataFrame".format(fifa_df.count()))

# Create a temporary view of fifa_df
fifa_df.createOrReplaceTempView('fifa_df_table')

# Construct the "query"
query = "SELECT Age FROM fifa_df_table WHERE Nationality == 'Germany'"

# Apply the SQL "query"
fifa_df_germany_age = spark.sql(query)

# Generate basic statistics
fifa_df_germany_age.describe().show()

# Convert fifa_df to fifa_df_germany_age_pandas DataFrame
fifa_df_germany_age_pandas = fifa_df_germany_age.toPandas()

# Plot the 'Age' density of Germany Players
fifa_df_germany_age_pandas.plot(kind='density')
plt.show()
