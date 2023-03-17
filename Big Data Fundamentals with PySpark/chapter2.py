from pyspark import SparkContext


sc = SparkContext(appName="MyApp")

# ex 1 "RDDs from Parallelized collections"
# Create an RDD from a list of words
RDD = sc.parallelize(
    ["Spark", "is", "a", "framework", "for", "Big Data processing"])

# Print out the type of the created object
print("The type of RDD is", type(RDD))


# ex 2 "RDDs from External Datasets"
file_path = "example_file_path"

# Print the file_path
print("The file_path is", file_path)

# Create a fileRDD from file_path
fileRDD = sc.textFile(file_path)

# Check the type of fileRDD
print("The file type of fileRDD is", type(fileRDD))


# ex 3 "Partitions in your data"
# Check the number of partitions in fileRDD
print("Number of partitions in fileRDD is", fileRDD.getNumPartitions())

# Create a fileRDD_part from file_path with 5 partitions
fileRDD_part = sc.textFile(file_path, minPartitions=5)

# Check the number of partitions in fileRDD_part
print("Number of partitions in fileRDD_part is",
      fileRDD_part.getNumPartitions())


# ex 4 "Map and Collect"
numbRDD = sc.parallelize(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Create map() transformation to cube numbers
cubedRDD = numbRDD.map(lambda x: x*x*x)

# Collect the results
numbers_all = cubedRDD.collect()

# Print the numbers from numbers_all
for numb in numbers_all:
    print(numb)


# ex 5 "Filter and Count"
# Filter the fileRDD to select lines with Spark keyword
fileRDD_filter = fileRDD.filter(lambda line: 'Spark' in line)

# How many lines are there in fileRDD?
print("The total number of lines with the keyword Spark is",
      fileRDD_filter.count())

# Print the first four lines of fileRDD
for line in fileRDD_filter.take(4):
    print(line)


# ex 6 "ReduceBykey and Collect"
# Create PairRDD Rdd with key value pairs
Rdd = sc.parallelize([(1, 2), (3, 4), (3, 6), (4, 5)])

# Apply reduceByKey() operation on Rdd
Rdd_Reduced = Rdd.reduceByKey(lambda x, y: x+y)

# Iterate over the result and print the output
for num in Rdd_Reduced.collect():
    print("Key {} has {} Counts".format(num[0], num[1]))


# ex 7 "SortByKey and Collect"
# Sort the reduced RDD with the key by descending order
Rdd_Reduced_Sort = Rdd_Reduced.sortByKey(ascending=False)

# Iterate over the result and retrieve all the elements of the RDD
for num in Rdd_Reduced_Sort.collect():
    print("Key {} has {} Counts".format(num[0], num[1]))


# ex 8 "CountingBykeys"
# Count the unique keys
total = Rdd.countByKey()

# What is the type of total?
print("The type of total is", type(total))

# Iterate over the total and print the output
for k, v in total.items():
    print("key", k, "has", v, "counts")


# ex 9 "Create a base RDD and transform it"
# Create a baseRDD from the file path
baseRDD = sc.textFile(
    "Complete_Shakespeare.txt")

# Split the lines of baseRDD into words
splitRDD = baseRDD.flatMap(lambda x: x.split())

# Count the total number of words
print("Total number of words in splitRDD:", splitRDD.count())

# ex 10 "Remove stop words and reduce the dataset"
stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves',
              'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him',
              'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its',
              'itself', 'they', 'them', 'their', 'theirs', 'themselves',
              'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those',
              'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have',
              'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an',
              'the', 'and', 'but', 'if', 'or', 'because', 'as',
              'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about',
              'against', 'between', 'into', 'through', 'during', 'before',
              'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in',
              'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then',
              'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all',
              'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some',
              'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than',
              'too', 'very', 'can', 'will', 'just', 'don', 'should', 'now']

# Convert the words in lower case and remove stop words from the stop_words
# curated list
splitRDD_no_stop = splitRDD.filter(
    lambda x: x.lower() not in stop_words)

# Create a tuple of the word and 1
splitRDD_no_stop_words = splitRDD_no_stop.map(lambda w: (w, 1))

# Count of the number of occurences of each word
resultRDD = splitRDD_no_stop_words.reduceByKey(lambda x, y: x + y)

# ex 11 "Print word frequencies"
# Display the first 10 words and their frequencies from the input RDD
for word in resultRDD.take(10):
    print(word)

# Swap the keys and values from the input RDD
resultRDD_swap = resultRDD.map(lambda x: (x[1], x[0]))

# Sort the keys in descending order
resultRDD_swap_sort = resultRDD_swap.sortByKey(ascending=False)

# Show the top 10 most frequent words and their frequencies from the sorted RDD
for word in resultRDD_swap_sort.take(10):
    print("{},{}". format(word[1], word[0]))
