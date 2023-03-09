import boto3
import pandas as pd


# ex 1 "Create a topic"
# Initialize boto3 client for SNS
sns = boto3.client('sns',
                   region_name='us-east-1',
                   aws_access_key_id=AWS_KEY_ID,
                   aws_secret_access_key=AWS_SECRET)

# Create the city_alerts topic
response = sns.create_topic(Name="city_alerts")
c_alerts_arn = response['TopicArn']

# Re-create the city_alerts topic using a oneliner
c_alerts_arn_1 = sns.create_topic(Name="city_alerts")['TopicArn']


# ex 2 "Create multiple topics"
sns = boto3.client('sns',
                   region_name='us-east-1',
                   aws_access_key_id=AWS_KEY_ID,
                   aws_secret_access_key=AWS_SECRET)

# Create list of departments
departments = ['trash', 'streets', 'water']

for dept in departments:
    # For every department, create a general topic
    sns.create_topic(Name="{}_general".format(dept))

    # For every department, create a critical topic
    sns.create_topic(Name="{}_critical".format(dept))

# Print all the topics in SNS
response = sns.list_topics()
print(response['Topics'])


# ex 3 "Deleting multiple topics"
sns = boto3.client('sns',
                   region_name='us-east-1',
                   aws_access_key_id=AWS_KEY_ID,
                   aws_secret_access_key=AWS_SECRET)

# Get the current list of topics
topics = sns.list_topics()['Topics']

for topic in topics:
    # For each topic, if it is not marked critical, delete it
    if "critical" not in topic['TopicArn']:
        sns.delete_topic(TopicArn=topic['TopicArn'])

# Print the list of remaining critical topics
print(sns.list_topics()['Topics'])


# ex 4 "Subscribing to topics"
sns = boto3.client('sns',
                   region_name='us-east-1',
                   aws_access_key_id=AWS_KEY_ID,
                   aws_secret_access_key=AWS_SECRET)

str_critical_arn = sns.create_topic(Name="streets_critical")['TopicArn']

# Subscribe phone number to streets_critical topic
resp_sms = sns.subscribe(
    TopicArn=str_critical_arn,
    Protocol='sms', Endpoint="+16196777733")

# Print the SubscriptionArn
print(resp_sms['SubscriptionArn'])

# Subscribe email to streets_critical topic.
resp_email = sns.subscribe(
    TopicArn=str_critical_arn,
    Protocol='email', Endpoint="eblock@sandiegocity.gov")

# Print the SubscriptionArn
print(resp_email['SubscriptionArn'])


# ex 5 "Create multiple subscriptions"
sns = boto3.client('sns',
                   region_name='us-east-1',
                   aws_access_key_id=AWS_KEY_ID,
                   aws_secret_access_key=AWS_SECRET)

str_critical_arn = sns.create_topic(Name="streets_critical")['TopicArn']

# For each email in contacts, create subscription to street_critical, contacts is a pd.DataFrame
for email in contacts['Email']:
    sns.subscribe(TopicArn=str_critical_arn,
                  Protocol='email',
                  Endpoint=email)

# List subscriptions for streets_critical topic, convert to DataFrame
response = sns.list_subscriptions_by_topic(
    TopicArn=str_critical_arn)
subs = pd.DataFrame(response['Subscriptions'])

# Preview the DataFrame
subs.head()


# ex 6 "Deleting multiple subscriptions"
sns = boto3.client('sns',
                   region_name='us-east-1',
                   aws_access_key_id=AWS_KEY_ID,
                   aws_secret_access_key=AWS_SECRET)

str_critical_arn = sns.create_topic(Name="streets_critical")['TopicArn']

# List subscriptions for streets_critical topic.
response = sns.list_subscriptions_by_topic(
    TopicArn=str_critical_arn)

# For each subscription, if the protocol is SMS, unsubscribe
for sub in response['Subscriptions']:
    if sub['Protocol'] == 'sms':
        sns.unsubscribe(SubscriptionArn=sub['SubscriptionArn'])

# List subscriptions for streets_critical topic in one line
subs = sns.list_subscriptions_by_topic(
    TopicArn=str_critical_arn)['Subscriptions']

# Print the subscriptions
print(subs)


# ex 7 "Sending an alert"
sns = boto3.client('sns',
                   region_name='us-east-1',
                   aws_access_key_id=AWS_KEY_ID,
                   aws_secret_access_key=AWS_SECRET)

str_critical_arn = sns.create_topic(Name="streets_critical")['TopicArn']

streets_v_count = 110
# If there are over 100 potholes, create a message
if streets_v_count > 100:
    message = "There are {} potholes!".format(streets_v_count)
    subject = "Latest pothole count is {}".format(streets_v_count)

    # Publish the email to the streets_critical topic
    sns.publish(
        TopicArn=str_critical_arn,
        Message=message,
        Subject=subject
    )


# ex 8 "Sending a single SMS message"
list_c = [['John Smith', 'js@fake.com', 11224567890, 'trash'], ['Janessa Goldsmith', 'whoami@fake.com', 11534567890, 'streets'], ['Evelyn Monroe', 'Evely@fake.com', 11234067890, 'water'], ['Max Pe', 'masdfsx@maksimize.com',
                                                                                                                                                                                             11234517890, 'water'], ['Fanny Mae', 'fanndyma3@fake.com', 11234597890, 'trash'], ['Janessa Goldsmith', 'whddsfsdoami@fake.com', 11534567890, 'water'], ['Max Pe', 'msdfsdfsdax@maksimize.com', 11234517890, 'streets']]
contacts = pd.DataFrame(
    list_c, columns=['Name', 'Email', 'Phone', 'Department'])

sns = boto3.client('sns',
                   region_name='us-east-1',
                   aws_access_key_id=AWS_KEY_ID,
                   aws_secret_access_key=AWS_SECRET)

# Loop through every row in contacts
for idx, row in contacts.iterrows():

    # Publish an ad-hoc sms to the user's phone number
    response = sns.publish(
        # Set the phone number
        PhoneNumber=str(row['Phone']),
        # The message should include the user's name
        Message='Hello {}'.format(row['Name'])
    )

    print(response)

b = contacts.values.tolist()
print(b)


# ex 9 "Case study"
sns = boto3.client('sns',
                   region_name='us-east-1',
                   aws_access_key_id=AWS_KEY_ID,
                   aws_secret_access_key=AWS_SECRET)

departments = ['trash' 'streets' 'water']

dept_arns = {}

for dept in departments:
    # For each deparment, create a critical topic
    critical = sns.create_topic(Name="{}_critical".format(dept))
    # For each department, create an extreme topic
    extreme = sns.create_topic(Name="{}_extreme".format(dept))
    # Place the created TopicARNs into a dictionary
    dept_arns['{}_critical'.format(dept)] = critical['TopicArn']
    dept_arns['{}_extreme'.format(dept)] = extreme['TopicArn']

# Print the filled dictionary.
print(dept_arns)

contacts = pd.DataFrame(
    list_c, columns=['Name', 'Email', 'Phone', 'Department'])

for index, user_row in contacts.iterrows():
    # Get topic names for the users's dept
    critical_tname = '{}_critical'.format(user_row['Department'])
    extreme_tname = '{}_extreme'.format(user_row['Department'])

    # Get or create the TopicArns for a user's department.
    critical_arn = sns.create_topic(Name=critical_tname)['TopicArn']
    extreme_arn = sns.create_topic(Name=extreme_tname)['TopicArn']

    # Subscribe each users email to the critical Topic
    sns.subscribe(TopicArn=critical_arn,
                  Protocol='email', Endpoint=user_row['Email'])
    # Subscribe each users phone number for the extreme Topic
    sns.subscribe(TopicArn=extreme_arn,
                  Protocol='sms', Endpoint=str(user_row['Phone']))


vcounts = {'trash': 100, 'streets': 422, 'water': 321}

if vcounts['water'] > 100:
    # If over 100 water violations, publish to water_critical
    sns.publish(
        TopicArn=dept_arns['water_critical'],
        Message="{} water issues".format(vcounts['water']),
        Subject="Help fix water violations NOW!")

if vcounts['water'] > 300:
    # If over 300 violations, publish to water_extreme
    sns.publish(
        TopicArn=dept_arns['water_extreme'],
        Message="{} violations! RUN!".format(vcounts['water']),
        Subject="THIS IS BAD.  WE ARE FLOODING!")
