from pyspark import SparkContext


# ex 1 "Understanding SparkContext"
sc = SparkContext(appName="MyApp")

# Print the version of SparkContext
print("The version of Spark Context in the PySpark shell is", sc.version)

# Print the Python version of SparkContext
print("The Python version of Spark Context in the PySpark shell is", 
      sc.pythonVer)

# Print the master of SparkContext
print("The master of Spark Context in the PySpark shell is", sc.master)


# ex 2 "Interactive Use of PySpark"
# Create a Python list of numbers from 1 to 100
numb = range(1, 101)

# Load the list into PySpark
spark_data = sc.parallelize(numb)


# ex 3 "Loading data in PySpark shell"
# Load a local file into PySpark shell
lines = sc.textFile("README.md")


# ex 4 "Use of lambda() with map()"
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print my_list in the console
print("Input list is", my_list)

# Square all numbers in my_list
squared_list_lambda = list(map(lambda x: x * x, my_list))

# Print the result of the map function
print("The squared numbers are", squared_list_lambda)


# ex 5 "Use of lambda() with filter()"
my_list2 = [10, 21, 31, 40, 51, 60, 72, 80, 93, 101]

# Print my_list2 in the console
print("Input list is:", my_list2)

# Filter numbers divisible by 10
filtered_list = list(filter(lambda x: (x % 10 == 0), my_list2))

# Print the numbers divisible by 10
print("Numbers divisible by 10 are:", filtered_list)
