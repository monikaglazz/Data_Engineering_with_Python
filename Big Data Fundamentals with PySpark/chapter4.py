from pyspark.mllib.clustering import KMeans
from pyspark.mllib.classification import LogisticRegressionWithLBFGS
from pyspark.mllib.recommendation import ALS, Rating
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.feature import HashingTF
from pyspark import SparkContext
from pyspark.sql import SparkSession
from math import sqrt
import matplotlib.pyplot as plt
import pandas as pd

sc = SparkContext(appName="MyApp")
spark = SparkSession.builder.getOrCreate()


# ex 1 "PySpark MLlib algorithms"
# Import the library for ALS
# Import the library for Logistic Regression
# Import the library for Kmeans


# ex 2 "Loading Movie Lens dataset into RDDs"
# Load the data into RDD
data = sc.textFile("ratings.csv")

# Split the RDD
ratings = data.map(lambda x: x.split(','))

# Transform the ratings RDD
ratings_final = ratings.map(lambda line: Rating(
    int(line[0]), int(line[1]), float(line[2])))

# Split the data into training and test
training_data, test_data = ratings_final.randomSplit([0.8, 0.2])


# ex 3 "Model training and predictions"
# Create the ALS model on the training data
model = ALS.train(training_data, rank=10, iterations=10)

# Drop the ratings column
testdata_no_rating = test_data.map(lambda p: (p[0], p[1]))

# Predict the model
predictions = model.predictAll(testdata_no_rating)

# Return the first 2 rows of the RDD
predictions.take(2)


# ex 4 "Model evaluation using MSE"
# Prepare ratings data
rates = ratings_final.map(lambda r: ((r[0], r[1]), r[2]))

# Prepare predictions data
preds = predictions.map(lambda r: ((r[0], r[1]), r[2]))

# Join the ratings data with predictions data
rates_and_preds = rates.join(preds)

# Calculate and print MSE
MSE = rates_and_preds.map(lambda r: (r[1][0] - r[1][1])**2).mean()
print(
    "Mean Squared Error of the model for the test data = {:.2f}".format(MSE))


# ex 5 "Loading spam and non-spam data"
# Load the datasets into RDDs
spam_rdd = sc.textFile("spam.txt")
non_spam_rdd = sc.textFile("ham.txt")

# Split the email messages into words
spam_words = spam_rdd.flatMap(lambda email: email.split(' '))
non_spam_words = non_spam_rdd.flatMap(lambda email: email.split(' '))

# Print the first element in the split RDD
print("The first element in spam_words is", spam_words.first())
print("The first element in non_spam_words is", non_spam_words.first())


# ex 6 "Feature hashing and LabelPoint"
# Create a HashingTf instance with 200 features
tf = HashingTF(numFeatures=200)

# Map each word to one feature
spam_features = tf.transform(spam_words)
non_spam_features = tf.transform(non_spam_words)

# Label the features: 1 for spam, 0 for non-spam
spam_samples = spam_features.map(
    lambda features: LabeledPoint(1, features))
non_spam_samples = non_spam_features.map(
    lambda features: LabeledPoint(0, features))

# Combine the two datasets
samples = spam_samples.join(non_spam_samples)


# ex 7 "Logistic Regression model training"
# Split the data into training and testing
train_samples, test_samples = samples.randomSplit([0.8, 0.2])

# Train the model
model = LogisticRegressionWithLBFGS.train(train_samples)

# Create a prediction label from the test data
predictions = model.predict(test_samples.map(lambda x: x.features))

# Combine original labels with the predicted labels
labels_and_preds = test_samples.map(lambda x: x.label).zip(predictions)

# Check the accuracy of the model on the test data
accuracy = labels_and_preds.filter(
    lambda x: x[0] == x[1]).count() / float(test_samples.count())
print("Model accuracy : {:.2f}".format(accuracy))


# ex 8 "Loading and parsing the 5000 points data"
# Load the dataset into an RDD
clusterRDD = sc.textFile("5000_points.txt")

# Split the RDD based on tab
rdd_split = clusterRDD.map(lambda x: x.split('\t'))

# Transform the split RDD by creating a list of integers
rdd_split_int = rdd_split.map(lambda x: [int(x[0]), int(x[1])])

# Count the number of rows in RDD
print("There are {} rows in the rdd_split_int dataset".format(
    rdd_split_int.count()))


# ex 9 "K-means training"
def error(point):
    center = model.centers[model.predict(point)]
    return sqrt(sum([x**2 for x in (point - center)]))


# Train the model with clusters from 13 to 16 and compute WSSSE
for clst in range(13, 17):
    model = KMeans.train(rdd_split_int, clst, seed=1)
    WSSSE = rdd_split_int.map(lambda point: error(
        point)).reduce(lambda x, y: x + y)
    print("The cluster {} has Within Set Sum of Squared Error {}".format(
        clst, WSSSE))

# Train the model again with the best k
model = KMeans.train(rdd_split_int, k=15, seed=1)

# Get cluster centers
cluster_centers = model.clusterCenters


# ex 10 "Visualizing clusters"
# Convert rdd_split_int RDD into Spark DataFrame and then to Pandas DataFrame
rdd_split_int_df_pandas = spark.createDataFrame(
    rdd_split_int, schema=["col1", "col2"]).toPandas()

# Convert cluster_centers to a pandas DataFrame
cluster_centers_pandas = pd.DataFrame(
    cluster_centers, columns=["col1", "col2"])

# Create an overlaid scatter plot of clusters and centroids
plt.scatter(rdd_split_int_df_pandas["col1"],
            rdd_split_int_df_pandas["col2"])
plt.scatter(cluster_centers_pandas["col1"],
            cluster_centers_pandas["col2"], color="red", marker="x")
plt.show()
