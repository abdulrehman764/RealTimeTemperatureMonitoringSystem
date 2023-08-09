import numpy as np
import time
from datetime import datetime
from faker import Faker
import pandas as pd
import boto3
import sys
import json
import base64

fake = Faker()


start_time = int(time.time())
end_time = time.time() + 600

number_of_devices = 3
areas = ['N', 'S', 'E', 'W']
desired_device_ids = ['ABC123', 'DEF456', 'GHI789']
# def get_device_ids_areas(number_of_devices):
#     # Universal Unique Identifier
#     return [(fake.uuid4(), areas[np.random.randint(0,4)]) for x in range(number_of_devices)]
def get_device_ids_areas(desired_device_ids):
    return [(device_id, areas[np.random.randint(0, 4)]) for device_id in desired_device_ids]

def convert_date_to_human_readable(unix_time):
    return datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S')

def get_temperature(previous_temperature = 22):
    # if previous_temperature % 2 == 0:
    #     return previous_temperature + np.random.randint(-2,5)
    # else:
    #     return previous_temperature + np.random.randint(-3,3)
    threshold = 50  # Threshold value for generating temperature above 50
    return np.random.randint(threshold, 101)
    # return np.random.randint(1, 101)


kinesis_client = boto3.client('kinesis', region_name='us-east-1')  # Replace with your AWS region


def send_temperature_to_stream(device_id, area, timestamp, temperature):
    stream_name = 'Abdul-Temperature-Stream'  # Replace with your Kinesis Data Stream name
    partition_key = device_id

    # Prepare the temperature data to be sent
    temperature_data = {
        'device_id': device_id,
        'area': area,
        'timestamp': timestamp,
        'temperature': temperature
    }

    # Convert the data to a JSON string
    json_data = json.dumps(temperature_data)

    # Base64 encode the JSON string
    encoded_data = base64.b64encode(json_data.encode('utf-8')).decode('utf-8')

    # Send the data to the Kinesis Data Stream
    response = kinesis_client.put_record(
        StreamName=stream_name,
        Data=json_data,
        PartitionKey=partition_key
    )

    # Print the response (useful for debugging)
    print(f"Data sent to Kinesis. ShardId: {response['ShardId']}, SequenceNumber: {response['SequenceNumber']}, Data: {json_data}")
    


def main():
    
    ids_areas = get_device_ids_areas(desired_device_ids )
    print(ids_areas)
    while True:
        for each_id, area in ids_areas:
            timestamp = convert_date_to_human_readable(int(time.time()))
            default_temperature = get_temperature()
            send_temperature_to_stream(each_id, area, timestamp, default_temperature)

        # Wait for 1 second before sending data for the next round
        time.sleep(5)


def lambda_handler(event, context):
    main()
