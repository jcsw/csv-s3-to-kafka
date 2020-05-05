from os import path
from boto3 import client

s3_client = client('s3')


def lambda_handler(event, context):
    record = event['Records'][0]
    bucket = record['s3']['bucket']['name']
    key = record['s3']['object']['key']
    print('bucket:{} key:{}'.format(bucket, key))

    input_file = path.join(bucket, key)
    with s3_client.open(input_file, 'r', newline='', encoding='utf-8-sig') as file:
        process_file(file)


def process_file(file):
    return None
