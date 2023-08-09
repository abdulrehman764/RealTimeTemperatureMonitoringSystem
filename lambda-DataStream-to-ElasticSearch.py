import base64
import boto3
import json
import requests
from requests_aws4auth import AWS4Auth

region = 'us-east-1'
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

host = 'https://search-abdul-es-lspe7ux6d7lu5pf2b2c3go2dkq.us-east-1.es.amazonaws.com'
index = 'temperature-data'
url = host + '/' + index + '/_doc/'  # Correctly specify the index and document type

headers = {"Content-Type": "application/json"}

def handler(event, context):
    count = 0
    for record in event['Records']:
        id = record['eventID']
        timestamp = record['kinesis']['approximateArrivalTimestamp']

        # Kinesis data is base64-encoded, so decode here
        message = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        print("message: ", message)

        # Convert the JSON string to a Python dictionary
        try:
            data = json.loads(message)
        except json.JSONDecodeError as e:
            print("Error decoding JSON:", e)
            continue

        # Create the JSON document
        document = {"id": id, "timestamp": timestamp, "message": data}
        print("document: ", document)
        print("url : ", url + id)  # Include the document ID in the URL

        # Index the document
        r = requests.put(url + id, auth=awsauth, json=document, headers=headers)
        count += 1
        print("status: ", r)
        print("status: ", r.status_code)
        print("response: ", r.json())

    return 'Processed ' + str(count) + ' items.'
