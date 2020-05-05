from boto3 import client
from urllib.parse import unquote_plus

s3_client = client('s3')


def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = unquote_plus(record['s3']['object']['key'])
        print('bucket:{} key:{}'.format(bucket, key))
