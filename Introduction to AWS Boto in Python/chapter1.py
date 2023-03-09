import boto3

# ex 1 "Create boto3 client"
s3 = boto3.client('s3', region_name='us-east-1',
                  # Set up AWS credentials
                  aws_access_key_id=AWS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET)
# List the buckets
buckets = s3.list_buckets()

print(buckets)


# ex 2 "Multiple clients"
s3 = boto3.client('s3', region_name='us-east-1',
                  aws_access_key_id=AWS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET)

sns = boto3.client('sns', region_name='us-east-1',
                   aws_access_key_id=AWS_KEY_ID,
                   aws_secret_access_key=AWS_SECRET)

# List S3 buckets and SNS topics
buckets = s3.list_buckets()
topics = sns.list_topics()

print(topics)


# ex 3 "Create the buckets"
s3 = boto3.client('s3', region_name='us-east-1',
                  aws_access_key_id=AWS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET)

response_staging = s3.create_bucket(Bucket='gim-staging')
response_processed = s3.create_bucket(Bucket='gim-processed')
response_test = s3.create_bucket(Bucket='gim-test')

# Print out the response
print(response_staging)


# ex 4 "Listing buckets"
s3 = boto3.client('s3', region_name='us-east-1',
                  aws_access_key_id=AWS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET)

buckets = s3.list_buckets()

for bucket in buckets['Buckets']:
    print(bucket['Name'])


# ex 5 "Deleting a bucket"
s3 = boto3.client('s3', region_name='us-east-1',
                  aws_access_key_id=AWS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET)

s3.delete_bucket(Bucket='gim-test')

response = s3.list_buckets()

for bucket in response['Buckets']:
    print(bucket['Name'])


# ex 6 "Deleting multiple buckets"
s3 = boto3.client('s3', region_name='us-east-1',
                  aws_access_key_id=AWS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET)

response = s3.list_buckets()

# Delete all the buckets with 'gim', create replacements.
for bucket in response['Buckets']:
    if 'gim' in bucket['Name']:
        s3.delete_bucket(Bucket=bucket['Name'])

s3.create_bucket(Bucket='gid-staging')
s3.create_bucket(Bucket='gid-processed')


# ex 7 "Putting files in the cloud"
# Upload final_report.csv with key 2019/final_report_01_01.csv
s3.upload_file(Bucket='gid-staging',
               Filename='final_report.csv',
               Key='2019/final_report_01_01.csv')

# Get object metadata and print it
response = s3.head_object(Bucket='gid-staging',
                          Key='2019/final_report_01_01.csv')

# Print the size of the uploaded object
print(response['ContentLength'])


# ex 8 "Delete files with prefix"
# List only objects that start with '2018/final_'
response = s3.list_objects(Bucket='gid-staging',
                           Prefix='2018/final_')

# Iterate over the objects and delete everyone
if 'Contents' in response:
    for obj in response['Contents']:
        # Delete the object
        s3.delete_object(Bucket='gid-staging', Key=obj['Key'])

# Print the keys of remaining objects in the bucket
response = s3.list_objects(Bucket='gid-staging')

for obj in response['Contents']:
    print(obj['Key'])
