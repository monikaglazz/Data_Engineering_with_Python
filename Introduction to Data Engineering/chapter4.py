import pandas as pd
from flask_sqlalchemy import SQLAlchemy as sqlalchemy

# 1

# Complete the connection URI
connection_uri = "postgresql://repl:password@localhost:5432/datacamp_application"
db_engine = sqlalchemy.create_engine(connection_uri)

# Get user with id 4387
user1 = pd.read_sql("SELECT * FROM rating WHERE user_id=4387", db_engine)

# Get user with id 18163
user2 = pd.read_sql("SELECT * FROM rating WHERE user_id=18163", db_engine)

# Get user with id 8770
user3 = pd.read_sql("SELECT * FROM rating WHERE user_id=8770", db_engine)


# 2

# CTransformation function
def transform_avg_rating(rating_data):
    # Group by course_id and extract average rating per course
    avg_rating = rating_data.groupby('course_id').rating.mean()
    # Return sorted average ratings per course
    sort_rating = avg_rating.sort_values(ascending=False).reset_index()
    return sort_rating


def extract_course_data(db_engines):
    return pd.read_sql("SELECT * FROM courses", db_engines)

# 3


# pandas data frame
course_data = extract_course_data(db_engine)

# Print out the number of missing values per column
print(course_data.isnull().sum())

# The transformation should fill in the missing values


def transform_fill_programming_language(course_data):
    imputed = course_data.fillna({"programming_language": "R"})
    return imputed


transformed = transform_fill_programming_language(course_data)

# Print out the number of missing values per column of transformed
print(transformed.isnull().sum())

# 4

# Complete the transformation function


def transform_recommendations(avg_course_ratings, courses_to_recommend):
    # Merge both DataFrames
    merged = courses_to_recommend.merge(avg_course_ratings)
    # Sort values by rating and group by user_id
    grouped = merged.sort_values("rating", ascending=False).groupby("user_id")
    # Produce the top 3 values and sort by user_id
    recommendations = grouped.head(3).sort_values("user_id").reset_index()
    final_recommendations = recommendations[["user_id", "course_id", "rating"]]
    # Return final recommendations
    return final_recommendations


# list with avg_course_ratings and courses_to_recommend
avg_course_ratings_l = [[46.0, 4.8], [23.0, 4.8], [96.0, 4.692765113974232], [56.0, 4.661764705882353], [24.0, 4.653061224489796], [26.0, 4.64625850340136], [61.0, 4.629213483146067], [85.0, 4.627118644067797], [87.0, 4.626373626373627], [81.0, 4.621338912133891], [31.0, 4.610208816705336], [86.0, 4.608695652173913], [7.0, 4.601471571906354], [44.0, 4.593866171003717], [14.0, 4.593220338983051], [76.0, 4.589743589743589], [35.0, 4.588235294117647], [37.0, 4.581818181818182], [71.0, 4.580645161290323], [28.0, 4.578947368421052], [32.0, 4.575687720915937], [3.0, 4.572611245256986], [95.0, 4.554395824969892], [25.0, 4.546875], [36.0, 4.546189868028948], [83.0, 4.545454545454546], [38.0, 4.542857142857143], [66.0, 4.540983606557377], [16.0, 4.5394736842105265], [1.0, 4.537634408602151], [33.0, 4.5353159851301115], [59.0, 4.535211267605634], [41.0, 4.533333333333333], [64.0, 4.532075471698113], [94.0, 4.529411764705882], [74.0, 4.529411764705882], [68.0, 4.5266272189349115], [63.0, 4.523809523809524], [75.0, 4.51948051948052], [60.0, 4.518918918918919], [91.0, 4.501621621621622], [6.0, 4.498025016458196], [49.0, 4.492537313432836], [90.0, 4.492190797804981], [11.0, 4.4860335195530725], [51.0, 4.484848484848484], [13.0, 4.478260869565218], [52.0, 4.477528089887641], [43.0, 4.4774774774774775], [
    34.0, 4.473684210526316], [9.0, 4.47008547008547], [22.0, 4.46218487394958], [84.0, 4.461538461538462], [50.0, 4.456913827655311], [67.0, 4.450236966824645], [88.0, 4.443298969072165], [40.0, 4.440366972477064], [65.0, 4.435714285714286], [78.0, 4.433333333333334], [45.0, 4.43298969072165], [21.0, 4.432835820895522], [55.0, 4.431818181818182], [27.0, 4.428571428571429], [70.0, 4.42814371257485], [58.0, 4.426724137931035], [48.0, 4.425925925925926], [53.0, 4.424242424242424], [93.0, 4.414634146341464], [57.0, 4.411764705882353], [30.0, 4.407407407407407], [82.0, 4.4], [39.0, 4.396551724137931], [79.0, 4.395833333333333], [99.0, 4.391304347826087], [20.0, 4.3712948517940715], [97.0, 4.365591397849462], [18.0, 4.353497164461247], [47.0, 4.35], [19.0, 4.347953216374269], [12.0, 4.340909090909091], [72.0, 4.340277777777778], [10.0, 4.339285714285714], [89.0, 4.338461538461538], [15.0, 4.3130434782608695], [4.0, 4.305232558139535], [80.0, 4.298913043478261], [69.0, 4.296], [73.0, 4.294117647058823], [62.0, 4.283018867924528], [100.0, 4.282608695652174], [5.0, 4.28125], [98.0, 4.269005847953216], [8.0, 4.257142857142857], [2.0, 4.253012048192771], [54.0, 4.238095238095238], [92.0, 4.222222222222222], [29.0, 4.208333333333333], [17.0, 4.147058823529412], [42.0, 4.107569721115538]]
courses_to_recommend_l = [[1, 64], [1, 60], [1, 73], [1, 79], [1, 85], [1, 94], [1, 61], [1, 5], [1, 11], [1, 22], [1, 47], [1, 41], [1, 25], [2, 13], [2, 9], [2, 24], [2, 31], [2, 77], [2, 83], [2, 91], [2, 37], [2, 38], [2, 48], [2, 55], [2, 61], [3, 4], [3, 74], [3, 50], [3, 89], [3, 63], [3, 5], [3, 12], [3, 24], [3, 41], [4, 15], [4, 54], [5, 73], [5, 79], [5, 85], [5, 94], [5, 81], [5, 58], [5, 10], [5, 16], [5, 25], [5, 57], [5, 46], [5, 38], [6, 54], [7, 68], [8, 6], [8, 70], [9, 98], [9, 88], [9, 72], [9, 17], [9, 43], [9, 33], [9, 21], [10, 30], [10, 33], [10, 43], [10, 59], [10, 72], [
    10, 88], [10, 97], [10, 19], [10, 26], [11, 15], [12, 95], [12, 14], [12, 19], [12, 88], [12, 32], [12, 40], [12, 59], [12, 72], [13, 90], [13, 92], [13, 98], [13, 72], [13, 56], [13, 34], [13, 21], [13, 39], [14, 68], [15, 68], [17, 65], [17, 29], [17, 46], [17, 81], [17, 58], [17, 51], [17, 23], [17, 74], [17, 80], [17, 22], [17, 13], [17, 10], [17, 4], [18, 68], [19, 30], [19, 14], [19, 19], [19, 40], [19, 93], [19, 75], [19, 66], [19, 44], [20, 30], [20, 72], [20, 66], [20, 44], [20, 34], [20, 100], [20, 88], [20, 95], [20, 1], [21, 96], [22, 30], [22, 18], [22, 14], [22, 97], [22, 100], [22, 75]]

# convert above lists to pandas data frame
avg_course_ratings = pd.DataFrame(
    avg_course_ratings_l, columns=['course_id', 'rating'])
courses_to_recommend = pd.DataFrame(
    courses_to_recommend_l, columns=['user_id', 'course_id'])

# Use the function
recommendations = transform_recommendations(
    avg_course_ratings, courses_to_recommend)


# 5

connection_uri = "postgresql://repl:password@localhost:5432/dwh"
db_engine = sqlalchemy.create_engine(connection_uri)


def load_to_dwh(recommendations):
    recommendations.to_sql("recommendations", db_engine, if_exists="replace")

# 6


# Define the DAG so it runs on a daily basis
dag = DAG(dag_id="recommendations",
          schedule_interval="0 0 * * *")

# Make sure `etl()` is called in the operator. Pass the correct kwargs.
task_recommendations = PythonOperator(
    task_id="recommendations_task",
    python_callable=etl,
    op_kwargs={"db_engines": db_engine},
)

# 7


def recommendations_for_user(user_id, threshold=4.5):
    # Join with the courses table
    query = """
    SELECT title, rating FROM recommendations
    INNER JOIN courses ON courses.course_id = recommendations.course_id
    WHERE user_id=%(user_id)s AND rating>%(threshold)s
    ORDER BY rating DESC
    """
    # Add the threshold parameter
    predictions_df = pd.read_sql(query, db_engine, params={"user_id": user_id,
                                                           "threshold": threshold})
    return predictions_df.title.values


# Try the function you created
print(recommendations_for_user(12, 4.65))
