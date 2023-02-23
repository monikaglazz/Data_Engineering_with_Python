import requests
import pandas as pd
from flask_sqlalchemy import SQLAlchemy as sqlalchemy
from pyspark.sql import SparkSession


# 1

# Fetch the Hackernews post
resp = requests.get("https://hacker-news.firebaseio.com/v0/item/16222426.json")

# Print the response parsed as JSON
print(resp.json())

# Assign the score of the test to post_score
post_score = resp.json()["score"]
print(post_score)


# 2

# Function to extract table to a pandas DataFrame
def extract_table_to_pandas(tablename, db_engine):
    query = "SELECT * FROM {}".format(tablename)
    return pd.read_sql(query, db_engine)


# Connect to the database using the connection URI
connection_uri = "postgresql://repl:password@localhost:5432/pagila"
db_engine = sqlalchemy.create_engine(connection_uri)

# Extract the film table into a pandas DataFrame
film_pandas_df = extract_table_to_pandas("film", db_engine)

# Extract the customer table into a pandas DataFrame
extract_table_to_pandas("customer", db_engine)


# 3

# convert pandas Data frame to PySpark data frame
spark = SparkSession.builder.appName("PandasToPySpark").getOrCreate()
film_df = spark.createDataFrame(film_pandas_df)


# 4

# Get the rental rate column as a string
rental_rate_str = film_df.rental_rate.astype("str")

# Split up and expand the column
rental_rate_expanded = rental_rate_str.rental_rate.split(".", expand=True)

# Assign the columns to film_df
film_df = film_df.assign(
    rental_rate_dollar=rental_rate_expanded[0],
    rental_rate_cents=rental_rate_expanded[1],
)

# 5

# list with ratings
ratings_list = [[0, 597, 5, 161], [1, 509, 4, 364], [2, 296, 5, 120], [3, 586, 5, 353], [4, 977, 5, 592], [5, 41, 5, 342], [6, 858, 4, 529], [7, 374, 4, 561], [8, 793, 5, 450], [9, 194, 5, 503], [10, 704, 5, 211], [11, 681, 5, 548], [12, 162, 5, 477], [13, 896, 4, 21], [14, 503, 4, 385], [15, 337, 5, 286], [16, 691, 5, 536], [17, 319, 5, 273], [18, 439, 5, 351], [19, 187, 5, 115], [20, 55, 5, 549], [21, 273, 5, 466], [22, 47, 5, 192], [23, 327, 2, 391], [24, 844, 2, 519], [25, 818, 5, 68], [26, 601, 4, 183], [27, 663, 2, 443], [28, 350, 5, 43], [29, 358, 5, 328], [30, 193, 5, 517], [31, 741, 5, 160], [32, 538, 4, 394], [33, 876, 3, 221], [34, 643, 4, 195], [35, 223, 5, 60], [36, 705, 3, 70], [37, 179, 4, 414], [38, 203, 3, 57], [39, 4, 4, 266], [40, 651, 5, 96], [41, 592, 5, 39], [42, 437, 5, 262], [43, 413, 5, 487], [44, 994, 5, 131], [45, 580, 3, 596], [46, 551, 5, 218], [47, 786, 4, 478], [48, 888, 4, 594], [49, 898, 5, 186], [
    50, 601, 5, 488], [51, 782, 5, 468], [52, 426, 4, 93], [53, 352, 5, 308], [54, 163, 5, 45], [55, 930, 5, 373], [56, 761, 5, 9], [57, 415, 5, 556], [58, 972, 5, 187], [59, 610, 5, 113], [60, 576, 4, 87], [61, 679, 3, 218], [62, 190, 5, 286], [63, 529, 5, 20], [64, 495, 2, 26], [65, 332, 5, 591], [66, 623, 4, 9], [67, 383, 5, 58], [68, 978, 3, 38], [69, 491, 1, 340], [70, 440, 5, 61], [71, 707, 5, 490], [72, 165, 5, 397], [73, 147, 5, 585], [74, 637, 5, 451], [75, 930, 5, 167], [76, 127, 5, 271], [77, 760, 5, 304], [78, 993, 5, 287], [79, 998, 4, 22], [80, 686, 5, 241], [81, 500, 4, 133], [82, 799, 5, 54], [83, 33, 4, 389], [84, 404, 5, 295], [85, 220, 4, 75], [86, 394, 3, 143], [87, 511, 4, 78], [88, 231, 4, 445], [89, 77, 5, 317], [90, 666, 3, 33], [91, 788, 5, 559], [92, 79, 3, 481], [93, 610, 5, 38], [94, 852, 5, 55], [95, 337, 4, 452], [96, 943, 5, 247], [97, 867, 3, 226], [98, 583, 5, 381], [99, 595, 5, 132]]

index = [sublist[0] for sublist in ratings_list]
data = [sublist[1:] for sublist in ratings_list]

# create pandas data frame for ratings
ratings_pandas_df = pd.DataFrame(data, index=index, columns=[
                                 '_c0', 'film_id', 'rating', 'customer_id'])

# create PySpark data frame for ratings
rating_df = spark.createDataFrame(ratings_pandas_df)


# 6

# Use groupBy and mean to aggregate the column
ratings_per_film_df = rating_df.groupBy('film_id').mean('rating')

# Join the tables using the film_id column
film_df_with_ratings = film_df.join(
    ratings_per_film_df,
    film_df.film_id == ratings_per_film_df.film_id
)

# Show the 5 first results
print(film_df_with_ratings.show(5))

# 7

# Write the pandas DataFrame to parquet
film_pandas_df.to_parquet("films_pdf.parquet")

# Write the PySpark DataFrame to parquet
film_df.write.parquet("films_sdf.parquet")

# 8

# connection URI
connection_uri = "postgresql://repl:password@localhost:5432/dwh"
db_engine_dwh = sqlalchemy.create_engine(connection_uri)

# list of list with recommendations
recom = [[842, 628, 112], [207, 390, 658], [589, 972], [416, 577], [491], [510, 205, 399], [388, 16, 794], [773], [833, 324, 219], [722], [940, 614], [478], [288], [61, 608], [333, 80, 147], [695, 939], [209, 168], [861], [137], [836, 941, 977], [911, 91, 949], [305], [126], [78, 573, 837], [546], [127, 279], [364, 116], [788, 818, 299], [871], [832, 615], [853, 88, 166], [539], [484, 440, 796], [58, 277], [372], [688, 954], [875, 527], [131], [137, 798, 504], [188], [981, 342, 862], [385, 218, 564], [626, 564, 575], [918], [590, 46], [164, 141], [800, 599, 299], [778], [487, 157], [328], [88, 810, 319], [
    764, 237], [901, 374, 852], [508, 655, 546], [630], [57, 210], [821, 422, 666], [425, 583], [119, 875, 317], [671, 253, 488], [331, 734, 51], [876, 951], [668, 702], [884], [41, 412], [345, 802], [868], [509, 412], [380, 365], [688], [798, 598, 998], [331], [256, 666, 680], [700, 4, 369], [469, 488], [220, 890], [35], [920, 213], [803, 654, 879], [770, 90, 924], [856], [117, 269], [992, 15, 622], [724, 248], [698, 110, 52], [342, 412, 879], [203, 903, 857], [337, 233, 397], [887], [746, 727], [562, 471], [82, 400, 631], [602, 679], [924], [35], [823, 445], [294, 132], [381, 876, 796], [789], [73, 87, 800]]

# create pandas series from list of lists
recommendations = pd.Series(data, index=index)

# Transformation step, join with recommendations data
film_pandas_df = film_pandas_df.join(recommendations)

# the .to_sql() call to write to store.film
film_pandas_df.to_sql("film", db_engine_dwh,
                      schema="store", if_exists="replace")

# Run the query to fetch the data
pd.read_sql("SELECT film_id, recommended_film_ids FROM store.film", db_engine_dwh)


# 9

# Finally whole process with proper functions

def extract_film_to_pandas():
    """Returns the extracted film table as a pandas DataFrame"""
    print("Extracting film table...")
    return pd.read_sql('SELECT * FROM film', db_engine)


def transform_rental_rate(film_df):
    """Takes a pandas DataFrame and returns the transformed DataFrame"""
    print("Transforming the rental_rate column...")
    rental_rate_str = film_df.rental_rate.astype("str")
    rental_rate_expanded = rental_rate_str.str.split(".", expand=True)
    return film_df.assign(
        rental_rate_dollar=rental_rate_expanded[0],
        rental_rate_cents=rental_rate_expanded[1],
    )


def load_dataframe_to_film(film_df):
    """Takes a pandas DataFrame and loads it into the film table in the data warehouse"""
    print("Loading film DataFrame to table...")
    film_df.to_sql("film", db_engine_dwh, schema="store", if_exists="replace")


# Define the example ETL function
def etl():
    film_df = extract_film_to_pandas()
    film_df = transform_rental_rate(film_df)
    load_dataframe_to_film(film_df)


# Define the ETL task using PythonOperator
etl_task = PythonOperator(task_id='etl_film',
                          python_callable=etl,
                          dag=dag)

# Set the upstream to wait_for_table and sample run etl()
etl_task.set_upstream(wait_for_table)
etl()
