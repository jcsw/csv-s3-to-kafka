from kafka import KafkaProducer

from app import config


class KafkaEngine:
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=[config.kafka_server.get()], retries=config.kafka_producer_retry.get())

    def send_to_csv_data_topic(self, key, data):
        future = self.producer.send('csv-data', key=key, value=data)
        record_metadata = future.get(config.kafka_producer_timeout.get())

        print(record_metadata.topic)
        print(record_metadata.partition)
        print(record_metadata.offset)

    def close(self):
        self.producer.flush(config.kafka_flush_timeout.get())
        self.producer.close(config.kafka_flush_timeout.get())
