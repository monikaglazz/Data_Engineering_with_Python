import boto3
import pandas as pd


# ex 1 "Cat detector"
rekog = boto3.client('recognition',
                     region_name='us-east-1',
                     aws_access_key_id=AWS_KEY_ID,
                     aws_secret_access_key=AWS_SECRET)

# Use Rekognition client to detect labels
image1_response = rekog.detect_labels(
    # Specify the image as an S3Object; Return one label
    Image=image1, MaxLabels=1)

# Print the labels
print(image1_response['Labels'])

# Use Rekognition client to detect labels
image2_response = rekog.detect_labels(Image=image2, MaxLabels=1)

# Print the labels
print(image2_response['Labels'])


# ex 2 "Multiple cat detector"
rekog = boto3.client('recognition',
                     region_name='us-east-1',
                     aws_access_key_id=AWS_KEY_ID,
                     aws_secret_access_key=AWS_SECRET)

response = rekog.detect_labels(
    # Specify the image as an S3Object; Return one label
    Image={'S3Object': {'Bucket': 'datacamp-img', 'Name': 'cats.jpg'}}, MaxLabels=1)

# Create an empty counter variable
cats_count = 0
# Iterate over the labels in the response
for label in response['Labels']:
    # Find the cat label, look over the detected instances
    if label['Name'] == 'Cat':
        for instance in label['Instances']:
            # Only count instances with confidence > 85
            if (instance['Confidence'] > 85):
                cats_count += 1
# Print count of cats
print(cats_count)


# ex 3 "Sign reader"
rekog = boto3.client('recognition',
                     region_name='us-east-1',
                     aws_access_key_id=AWS_KEY_ID,
                     aws_secret_access_key=AWS_SECRET)

response = rekog.detect_text(
    Image={'S3Object': {'Bucket': 'datacamp-img', 'Name': 'report.jpg'}})

# Create empty list of words
words = []
# Iterate over the TextDetections in the response dictionary
for text_detection in response['TextDetections']:
    # If TextDetection type is WORD, append it to words list
    if text_detection['Type'] == 'WORD':
        # Append the detected text
        words.append(text_detection['DetectedText'])
# Print out the words list
print(words)

# Create empty list of lines
lines = []
# Iterate over the TextDetections in the response dictionary
for text_detection in response['TextDetections']:
    # If TextDetection type is Line, append it to lines list
    if text_detection['Type'] == 'LINE':
        # Append the detected text
        lines.append(text_detection['DetectedText'])
# Print out the words list
print(lines)


# ex 4 ""
lists = [[93494, 'Illegal Dumping', "Bales of hay & pallets, old cars, hoarding issue. Fire hazard the picture doesn't do it justice. A junk yard within a neighborhood."], [101502, 'Illegal Dumping', 'Couch, 4 chairs, mattress, carpet padding. this is a on going problem'], [101520, 'Illegal Dumping', ''], [101576, 'Illegal Dumping', 'On the South Side of Paradise Valley Road near the intersection with Jester St. Stuff in trash bags, rolling suitcases, and shopping carts. I suspect possessions of folk camping in the canyon.'], [101616, 'Illegal Dumping', 'Hay un campamento para personas sin hogar en los acantilados al final de la Avenida Del Mar en Ocean Beach. Mucha basura, estructura similar a la tienda, almohadas, ropa y heces humanas. Vi a un hombre esta ma–ana salir del acantilado excavando el acantilado. Parece que ha estado dando pasos para facilitar su descenso a su campamento. No estaba seguro de c—mo responder a la pregunta de materiales peligrosos. Hay heces humanas visibles, as’ que respond’ que s’.'], [101648, 'Illegal Dumping', 'Litter everywhere where homeless camps.  Balboa park. Trail going down to pedestrian bridge across 163 and Marston house'], [101727, 'Illegal Dumping', 'Hay basura por todas partes a lo largo de la carretera. Parece que tambiŽn hay un campamento ilegal de personas sin hogar en la zona.'], [101841, 'Illegal Dumping', 'Homeless camp active within state highway fencing nb163 behind Ralphs.  Trash, tents, garbage strewn down the hill, drug dealing prostitution etc.'], [101846, 'Illegal Dumping', 'Hay una basura a lo largo del borde del ca–—n. Cada vez m‡s basura aparecen todos los d’as.'], [101879, 'Illegal Dumping', "There is a freezer, lawn mowers. bed frame, vacuum cleaners, dressers and entertainment centers in the front yard looks like a junk yard. tenent has put salvation army signs on the junk. the salvation army truck came and wouldn't take  the items."], [101918, 'Illegal Dumping', 'Neum‡tico y otros art’culos en la ladera del ca–—n al norte de Marlton.'], [102017, 'Illegal Dumping', 'Homeless Camp at 37th Street Paper street at Myrtle Avenue (3693 Myrtle Ave. overlooking 15 freeway, immediately adjacent to homes.'], [102023, 'Illegal Dumping', 'On Old Sea World Drive & Friars to South Shores Parkway (and possibly beyond to the Jetty) there are several spots where illegal dumping has occurred.'], [102056, 'Illegal Dumping', ''], [102089, 'Illegal Dumping', 'Test'], [102176, 'Illegal Dumping', 'The city easement is littered with trash between Villa Europa HOA and Axiom (Trieste) apartments.  Please have a crew clean the area.'], [
    102196, 'Illegal Dumping', 'Two encampments, one in the park (red umbrella), the other down the embankment (east) toward the 163.   I think this is "Cypress Grove" area.'], [102198, 'Illegal Dumping', 'Enorme cantidad de escombros / basura / vertimiento a lo largo de la valla de eslabones de cadena Marston en el lado del Parque Balboa en el extremo este, cerca del sendero que conduce al ca–—n. La valla tambiŽn est‡ cortada.'], [102199, 'Illegal Dumping', 'El ‡rea no est‡ en el mapa. Donde est‡ el pin, ir al norte a lo largo de la carretera tan lejos al norte como usted puede ir (parece ser el sendero nupcial) (la parte m‡s norte del Balboa Park/Marston Property hay algunos ‡rboles ca’dos y un enorme desastre y 2 campamentos. La valla del eslab—n norte est‡ cortada.'], [102242, 'Illegal Dumping', 'Illegal campsites,litter trash drug dealing'], [102282, 'Illegal Dumping', 'Beginning or end of rose creek path there is a ton of trash down here. Not to mention the homeless people doing drugs on the path under the bridge. This is a beautiful path that should be cleaned up.'], [102382, 'Illegal Dumping', ''], [102403, 'Illegal Dumping', 'Remove tree debris from fwy slope'], [102457, 'Illegal Dumping', ''], [102462, 'Illegal Dumping', 'Large amount of trash,  etc'], [102464, 'Illegal Dumping', 'Trash active camp illegal activity'], [102465, 'Illegal Dumping', 'Active camp tents. Behind Ralphs on state highway property'], [102541, 'Illegal Dumping', 'Los residentes de 2604 46th St (en la comunidad de City Heights) descarten ilegalmente una gran cantidad de basura en la acera pœblica y el ca–—n. Revise las im‡genes para referencia. Gracias por su atenci—n con este asunto serio y la mejora de la comunidad.'], [102634, 'Illegal Dumping', 'I suspect you receive constant reports of trash piling up at this location, as there are constantly piles of trash just a few steps from the street (and on down into the canyon).'], [102638, 'Illegal Dumping', 'Objetos personales abandonados'], [102661, 'Illegal Dumping', 'Tents setup in famous slough, north of w pt Loma blvd. 100 yards up path, 2 tents all week'], [102760, 'Illegal Dumping', 'Jeremy Henwood City Heights Park encampments'], [102761, 'Illegal Dumping', 'Jeremy Henwood City Heights Park EncampmentPersonal belongings, overnight camping.'], [102775, 'Illegal Dumping', ''], [102851, 'Illegal Dumping', 'Litter grocery carts chairs. Clothing homeless.   You should clean up the homeless camps in this area'], [102853, 'Illegal Dumping', 'Abandoned mattresses homeless'], [102854, 'Illegal Dumping', 'Homeless active camp litter erx']]
dumping_df = pd.DataFrame(
    lists, colums=['service_request_id', 'service_name', 'public_description'])

comprehend = boto3.client('comprehend',
                          region_name='us-east-1',
                          aws_access_key_id=AWS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET)

# For each dataframe row
for index, row in dumping_df.iterrows():
    # Get the public description field
    description = dumping_df.loc[index, 'public_description']
    if description != '':
        # Detect language in the field content
        resp = comprehend.detect_dominant_language(Text=description)
        # Assign the top choice language to the lang column.
        dumping_df.loc[index, 'lang'] = resp['Languages'][0]['LanguageCode']

# Count the total number of spanish posts
spanish_post_ct = len(dumping_df[dumping_df.lang == 'es'])
# Print the result
print("{} posts in Spanish".format(spanish_post_ct))


# ex 5 "Translating text"
translate = boto3.client('translate',
                         region_name='us-east-1',
                         aws_access_key_id=AWS_KEY_ID,
                         aws_secret_access_key=AWS_SECRET)

for index, row in dumping_df.iterrows():
    # Get the public_description into a variable
    description = dumping_df.loc[index, 'public_description']
    if description != '':
        # Translate the public description
        resp = translate.translate_text(
            Text=description,
            SourceLanguageCode='auto', TargetLanguageCode='en')
        # Store original language in original_lang column
        dumping_df.loc[index, 'original_lang'] = resp['SourceLanguageCode']
        # Store the translation in the translated_desc column
        dumping_df.loc[index, 'translated_desc'] = resp['TranslatedText']
# Preview the resulting DataFrame
dumping_df = dumping_df[['service_request_id',
                         'original_lang', 'translated_desc']]
dumping_df.head()


# ex 6 "Getting request sentiment"
comprehend = boto3.client('comprehend',
                          region_name='us-east-1',
                          aws_access_key_id=AWS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET)

for index, row in dumping_df.iterrows():
    # Get the translated_desc into a variable
    description = dumping_df.loc[index, 'public_description']
    if description != '':
        # Get the detect_sentiment response
        response = comprehend.detect_sentiment(
            Text=description,
            LanguageCode='en')
        # Get the sentiment key value into sentiment column
        dumping_df.loc[index, 'sentiment'] = response['Sentiment']
# Preview the dataframe
dumping_df.head()


# ex 7 "Case Study"
data = [[93494, 'Illegal Dumping', 'Hay un scooter electrico en sidewalk'], [101502, 'Illegal Dumping', 'Chi_c xe tay ga ch_n v_a h\x8f vˆ t™i kh™ng th_ _i qua xe l_n'], [101520, 'Illegal Dumping', 'There is a scooter blocking the sidewalk '], [101576, 'Illegal Dumping', 'I tripped on a stupid scooter'], [101576, 'Illegal Dumping', 'Hay un scooter electrico en sidewalk'], [101502, 'Illegal Dumping', 'Gustung-gusto ko ang mga scooter'], [101502, 'Illegal Dumping', 'There is a scooter blocking the sidewalk '], [101502, 'Illegal Dumping', 'Chi_c xe tay ga ch_n v_a h\x8f vˆ t™i kh™ng th_ _i qua xe l_n'], [101576, 'Illegal Dumping', 'This scooter helped me move a mattress! '], [101576, 'Illegal Dumping', 'Hay un scooter electrico en sidewalk'], [101502, 'Illegal Dumping', 'Gustung-gusto ko ang mga scooter'], [93494, 'Illegal Dumping', 'Hay un scooter electrico en sidewalk'], [101502, 'Illegal Dumping', 'Chi_c xe tay ga ch_n v_a h\x8f vˆ t™i kh™ng th_ _i qua xe l_n'], [101520, 'Illegal Dumping', 'There is a scooter blocking the sidewalk '], [101576, 'Illegal Dumping', 'I tripped on a stupid scooter'], [101576, 'Illegal Dumping', 'Hay un scooter electrico en sidewalk'], [101502, 'Illegal Dumping', 'Gustung-gusto ko ang mga scooter'], [101502, 'Illegal Dumping', 'There is a scooter blocking the sidewalk '], [101502, 'Illegal Dumping', 'Chi_c xe tay ga ch_n v_a h\x8f vˆ t™i kh™ng th_ _i qua xe l_n'], [101576, 'Illegal Dumping', 'This scooter helped me move a mattress! '], [101576, 'Illegal Dumping', 'Hay un scooter electrico en sidewalk'], [101502, 'Illegal Dumping', 'Gustung-gusto ko ang mga scooter'], [101502, 'Illegal Dumping', 'Chi_c xe tay ga ch_n v_a h\x8f vˆ t™i kh™ng th_ _i qua xe l_n'], [101502, 'Illegal Dumping', 'Chi_c xe tay ga ch_n v_a h\x8f vˆ t™i kh™ng th_ _i qua xe l_n'], [101502, 'Illegal Dumping', 'Chi_c xe tay ga ch_n v_a h\x8f vˆ t™i kh™ng th_ _i qua xe l_n'], [101502, 'Illegal Dumping', 'Chi_c xe tay ga ch_n v_a h\x8f vˆ t™i kh™ng th_ _i qua xe l_n'], [101502, 'Illegal Dumping', 'Chi_c xe tay ga ch_n v_a h\x8f vˆ t™i kh™ng th_ _i qua xe l_n'], [101502, 'Illegal Dumping', 'Chi_c xe tay ga ch_n v_a h\x8f vˆ t™i kh™ng th_ _i qua xe l_n'], [101502, 'Illegal Dumping', 'Chi_c xe tay ga ch_n v_a h\x8f vˆ t™i kh™ng th_ _i qua xe l_n'], [101502, 'Illegal Dumping', 'Chi_c xe tay ga ch_n v_a h\x8f vˆ t™i kh™ng th_ _i qua xe l_n'], [101502, 'Illegal Dumping', 'Chi_c xe tay ga ch_n v_a h\x8f vˆ t™i kh™ng th_ _i qua xe l_n'], [101502, 'Illegal Dumping', 'Chi_c xe tay ga ch_n v_a h\x8f vˆ t™i kh™ng th_ _i qua xe l_n'],
        [101502, 'Illegal Dumping', 'Chi_c xe tay ga ch_n v_a h\x8f vˆ t™i kh™ng th_ _i qua xe l_n'], [101502, 'Illegal Dumping', 'Chi_c xe tay ga ch_n v_a h\x8f vˆ t™i kh™ng th_ _i qua xe l_n'], [101502, 'Illegal Dumping', 'Chi_c xe tay ga ch_n v_a h\x8f vˆ t™i kh™ng th_ _i qua xe l_n'], [101502, 'Illegal Dumping', 'Chi_c xe tay ga ch_n v_a h\x8f vˆ t™i kh™ng th_ _i qua xe l_n'], [101502, 'Illegal Dumping', 'Chi_c xe tay ga ch_n v_a h\x8f vˆ t™i kh™ng th_ _i qua xe l_n'], [101502, 'Illegal Dumping', 'Chi_c xe tay ga ch_n v_a h\x8f vˆ t™i kh™ng th_ _i qua xe l_n'], [101502, 'Illegal Dumping', 'Chi_c xe tay ga ch_n v_a h\x8f vˆ t™i kh™ng th_ _i qua xe l_n'], [101502, 'Illegal Dumping', 'Chi_c xe tay ga ch_n v_a h\x8f vˆ t™i kh™ng th_ _i qua xe l_n'], [101502, 'Illegal Dumping', 'Chi_c xe tay ga ch_n v_a h\x8f vˆ t™i kh™ng th_ _i qua xe l_n'], [101502, 'Illegal Dumping', 'Chi_c xe tay ga ch_n v_a h\x8f vˆ t™i kh™ng th_ _i qua xe l_n'], [101502, 'Illegal Dumping', 'Gustung-gusto ko ang mga scooter'], [101502, 'Illegal Dumping', 'Gustung-gusto ko ang mga scooter'], [101502, 'Illegal Dumping', 'Gustung-gusto ko ang mga scooter'], [101502, 'Illegal Dumping', 'Gustung-gusto ko ang mga scooter'], [101502, 'Illegal Dumping', 'Gustung-gusto ko ang mga scooter'], [101502, 'Illegal Dumping', 'Gustung-gusto ko ang mga scooter'], [101502, 'Illegal Dumping', 'Gustung-gusto ko ang mga scooter'], [101502, 'Illegal Dumping', 'Gustung-gusto ko ang mga scooter'], [101502, 'Illegal Dumping', 'Gustung-gusto ko ang mga scooter'], [101502, 'Illegal Dumping', 'Gustung-gusto ko ang mga scooter'], [101502, 'Illegal Dumping', 'Gustung-gusto ko ang mga scooter'], [101502, 'Illegal Dumping', 'Gustung-gusto ko ang mga scooter'], [101502, 'Illegal Dumping', 'Gustung-gusto ko ang mga scooter'], [101502, 'Illegal Dumping', 'Gustung-gusto ko ang mga scooter'], [101502, 'Illegal Dumping', 'Gustung-gusto ko ang mga scooter'], [101502, 'Illegal Dumping', 'Gustung-gusto ko ang mga scooter'], [101502, 'Illegal Dumping', 'Gustung-gusto ko ang mga scooter'], [101502, 'Illegal Dumping', 'Gustung-gusto ko ang mga scooter'], [101502, 'Illegal Dumping', 'Gustung-gusto ko ang mga scooter'], [101502, 'Illegal Dumping', 'Gustung-gusto ko ang mga scooter'], [101502, 'Illegal Dumping', 'Gustung-gusto ko ang mga scooter'], [101502, 'Illegal Dumping', 'Gustung-gusto ko ang mga scooter'], [101502, 'Illegal Dumping', 'Gustung-gusto ko ang mga scooter'], [101502, 'Illegal Dumping', 'Gustung-gusto ko ang mga scooter'], [101502, 'Illegal Dumping', 'Gustung-gusto ko ang mga scooter']]
scooter_df = pd.DataFrame(
    data, colums=['service_request_id', 'service_name', 'public_description'])

comprehend = boto3.client('comprehend',
                          region_name='us-east-1',
                          aws_access_key_id=AWS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET)

for index, row in scooter_df.iterrows():
    # For every DataFrame row
    desc = scooter_df.loc[index, 'public_description']
    if desc != '':
        # Detect the dominant language
        resp = comprehend.detect_dominant_language(Text=desc)
        lang_code = resp['Languages'][0]['LanguageCode']
        scooter_df.loc[index, 'lang'] = lang_code
        # Use the detected language to determine sentiment
        scooter_df.loc[index, 'sentiment'] = comprehend.detect_sentiment(
            Text=desc,
            LanguageCode=lang_code)['Sentiment']
# Perform a count of sentiment by group.
counts = scooter_df.groupby(['sentiment', 'lang']).count()
counts.head()

data2 = [[101520, '2016-08-24T16:14:00', 'Illegal Dumping', 1, 32.77605567, -117.100004, 'POSITIVE', 'There is a scooter blocking the sidewalk '], [101502, '2016-08-24T14:48:00', 'Illegal Dumping', 1, 32.7077658, -117.1281408, 'NEGATIVE', 'There is a scooter blocking the sidewalk '], [101576, '2016-08-24T21:28:00', 'Illegal Dumping', 0, 32.68899358, -117.0584723, 'POSITIVE', 'This scooter helped me move a mattress! '], [101520, '2016-08-24T16:14:00', 'Illegal Dumping', 1,
                                                                                                                                                                                                                                                                                                                                                                                                                                        32.77605567, -117.100004, 'NEGATIVE', 'There is a scooter blocking the sidewalk '], [101576, '2016-08-24T21:28:00', 'Illegal Dumping', 1, 32.68899358, -117.0584723, 'POSITIVE', 'I tripped on a stupid scooter'], [101502, '2016-08-24T14:48:00', 'Illegal Dumping', 0, 32.7077658, -117.1281408, 'NEGATIVE', 'There is a scooter blocking the sidewalk '], [101576, '2016-08-24T21:28:00', 'Illegal Dumping', 1, 32.68899358, -117.0584723, 'NEGATIVE', 'This scooter helped me move a mattress! ']]
scooter_requests = pd.DataFrame(data2, columns=['service_request_id', 'requested_datetime',
                                'service_name', 'img_scooter', 'lat', 'long', 'sentiment', 'public_description'])

sns = boto3.client('sns',
                   region_name='us-east-1',
                   aws_access_key_id=AWS_KEY_ID,
                   aws_secret_access_key=AWS_SECRET)

# Get topic ARN for scooter notifications
topic_arn = sns.create_topic(Name='scooter_notifications')['TopicArn']

for index, row in scooter_requests.iterrows():
    # Check if notification should be sent
    if (row['sentiment'] == 'NEGATIVE') & (row['img_scooter'] == 1):
        # Construct a message to publish to the scooter team.
        message = "Please remove scooter at {}, {}. Description: {}".format(
            row['long'], row['lat'], row['public_description'])

        # Publish the message to the topic!
        sns.publish(TopicArn=topic_arn,
                    Message=message,
                    Subject="Scooter Alert")
