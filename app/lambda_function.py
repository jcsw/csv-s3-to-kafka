from os import path
from boto3 import client

from app import config
from app import kafka_engine
from app import csv_engine

s3_client = client('s3')


def lambda_handler(event, context):
    config.init()

    record = event['Records'][0]
    bucket = record['s3']['bucket']['name']
    key = record['s3']['object']['key']
    print('bucket:{} key:{}'.format(bucket, key))

    input_file = path.join(bucket, key)
    with s3_client.open(input_file, 'r', newline='', encoding='utf-8-sig') as file:
        process_file(file)


def process_file(file):
    kafka = kafka_engine.KafkaEngine()
    on_line = lambda line: kafka.send_to_csv_data_topic(line[0], line)

    csv = csv_engine.CsvEngine(file)
    count = csv.process_csv(on_line)
    print(count)

    kafka.close()
