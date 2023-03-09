import boto3
import pandas as pd


# ex 1 "Upload a public file"
s3 = boto3.client('s3', region_name='us-east-1',
                  aws_access_key_id=AWS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET)

s3.upload_file(
    Filename='./final_report.csv',
    Key='2019/final_report_2019_02_20.csv',
    Bucket='gid-staging',
    ExtraArgs={
        'ACL': 'public-read'})


# ex 2 "Making multiple files public"
# List only objects that start with '2019/final_'
response = s3.list_objects(
    Bucket='gid-staging', Prefix='2019/final_')

# Iterate over the objects
for obj in response['Contents']:

    # Give each object ACL of public-read
    s3.put_object_acl(Bucket='gid-staging',
                      Key=obj['Key'],
                      ACL='public-read')

    # Print the Public Object URL for each object
    print("https://{}.s3.amazonaws.com/{}".format('gid-staging', obj['Key']))


# ex 3 "Generating a presigned URL"
s3 = boto3.client('s3', region_name='us-east-1',
                  aws_access_key_id=AWS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET)

share_url = s3.generate_presigned_url(
    # Specify allowable operations
    ClientMethod='get_object',
    # Set the expiration time
    ExpiresIn=3600,
    # Set bucket and shareable object's name
    Params={'Bucket': 'gid-staging', 'Key': 'final_report.csv'}
)

# Print out the presigned URL
print(share_url)


# ex 4 "Reading private files into pandas and concatenating them into one DataFrame"
s3 = boto3.client('s3', region_name='us-east-1',
                  aws_access_key_id=AWS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET)

response = s3.list_objects(Bucket='gid-requests', Prefix='2019')

df_list = []

for file in response['Contents']:
    # For each file in response load the object from S3
    obj = s3.get_object(Bucket='gid-requests', Key=file['Key'])
    # Load the object's StreamingBody with pandas
    obj_df = pd.read_csv(obj['Body'])
    # Append the resulting DataFrame to list
    df_list.append(obj_df)

# Concat all the DataFrames with pandas
df = pd.concat(df_list)

# Preview the resulting DataFrame
df.head()


# ex 5 "Generate HTML table from Pandas"
services_list = [['Abandoned Vehicle', 'Other', 'https://www.sandiego.gov/get-it-done'], ['Light On During Day', 'Street Light', 'https://www.sandiego.gov/get-it-done'], ['Curb', 'Streets', 'https://www.sandiego.gov/get-it-done'], ['All Lights Out', 'Traffic Signal', 'https://www.sandiego.gov/get-it-done'], ['Storm Drain', 'Storm Water', 'https://www.sandiego.gov/get-it-done'], ['Light Out', 'Street Light', 'https://www.sandiego.gov/get-it-done'], ['Flashing Red', 'Traffic Signal', 'https://www.sandiego.gov/get-it-done'], ['Dead Animal', 'Other', 'https://www.sandiego.gov/get-it-done'], ['Damaged Guardrail', 'Streets', 'https://www.sandiego.gov/get-it-done'], ['Street Flooded', 'Storm Water', 'https://www.sandiego.gov/get-it-done'], ['Light Out', 'Traffic Signal', 'https://www.sandiego.gov/get-it-done'], ['Graffiti', 'Other',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 'https://www.sandiego.gov/get-it-done'], ['Faded striping', 'Streets', 'https://www.sandiego.gov/get-it-done'], ['Signal Facing Wrong Direction', 'Traffic Signal', 'https://www.sandiego.gov/get-it-done'], ['Parking Meter', 'Streets', 'https://www.sandiego.gov/get-it-done'], ['Litter - Open Space/Canyon/Park', 'Other', 'https://www.sandiego.gov/get-it-done'], ['Litter - Street/Sidewalk', 'Other', 'https://www.sandiego.gov/get-it-done'], ['Pothole', 'Streets', 'https://www.sandiego.gov/get-it-done'], ['Tree Hazard', 'Other', 'https://www.sandiego.gov/get-it-done'], ['Sidewalk', 'Streets', 'https://www.sandiego.gov/get-it-done'], ['Street Sweeping', 'Streets', 'https://www.sandiego.gov/get-it-done'], ['Traffic Sign', 'Streets', 'https://www.sandiego.gov/get-it-done'], ['Other', 'Other', 'https://www.sandiego.gov/get-it-done']]
services_df = pd.DataFrame(services_list, columns=[
                           'service_name', 'group', 'link'])

# Generate an HTML table with no border and selected columns
services_df.to_html('./services_no_border.html',
                    # Keep specific columns only
                    columns=['service_name', 'link'],
                    # Set border
                    border=0)

# Generate an html table with border and all columns.
services_df.to_html('./services_border_all_columns.html',
                    columns=['service_name', 'group', 'link'],
                    border=1)


# ex 6 "Upload an HTML file to S3"
s3 = boto3.client('s3', region_name='us-east-1',
                  aws_access_key_id=AWS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET)

# Upload the lines.html file to S3
s3.upload_file(Filename='lines.html',
               Bucket='datacamp-public', Key='index.html',
               ExtraArgs={
                   'ContentType': 'text/html',
                   'ACL': 'public-read'})

print("http://{}.s3.amazonaws.com/{}".format('datacamp-public', 'index.html'))


# ex 7 "Case study"
s3 = boto3.client('s3', region_name='us-east-1',
                  aws_access_key_id=AWS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET)

response = s3.list_objects(Bucket='gid-requests', Prefix='2019_feb')
request_files = response['Contents']

df_list = []

for file in request_files:
    s3_day_reqs = s3.get_object(Bucket='gid-requests',
                                Key=file['Key'])
    day_reqs = pd.read_csv(s3_day_reqs['Body'])
    df_list.append(day_reqs)

all_reqs = pd.concat(df_list)

agg_df = all_reqs.groupby(['service_name'])['service_name'].count()

# Write agg_df to a CSV and HTML file with no border
agg_df.to_csv('./feb_final_report.csv')
agg_df.to_html('./feb_final_report.html', border=0)

# Upload the generated CSV to the gid-reports bucket
s3.upload_file(Filename='./feb_final_report.csv',
               Key='2019/feb/final_report.html', Bucket='gid-reports',
               ExtraArgs={'ACL': 'public-read'})

# Upload the generated HTML to the gid-reports bucket
s3.upload_file(Filename='./feb_final_report.html',
               Key='2019/feb/final_report.html', Bucket='gid-reports',
               ExtraArgs={'ContentType': 'text/html',
                          'ACL': 'public-read'})

# List the gid-reports bucket objects starting with 2019/
objects_list = s3.list_objects(Bucket='gid-reports', Prefix='2019/')

# Convert the response contents to DataFrame
objects_df = pd.DataFrame(objects_list['Contents'])

# Create a column "Link" that contains Public Object URL
base_url = "http://gid-reports.s3.amazonaws.com/"
objects_df['Link'] = base_url + objects_df['Key']

# Preview the resulting DataFrame
objects_df.head()

# Write objects_df to an HTML file
objects_df.to_html('report_listing.html',
                   render_links=True,
                   columns=['Link', 'LastModified', 'Size'])

# Overwrite index.html key by uploading the new file
s3.upload_file(
    Filename='./report_listing.html', Key='index.html',
    Bucket='gid-reports',
    ExtraArgs={
        'ContentType': 'text/html',
        'ACL': 'public-read'
    })
