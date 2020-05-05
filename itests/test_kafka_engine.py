from unittest import TestCase
from mock import patch
from random import randint

from app import kafka_engine
from app import config


class KafkaEngineTest(TestCase):

    @patch.dict('os.environ',
                     {'kafka_server': 'localhost',
                      'kafka_producer_timeout': '3',
                      'kafka_producer_retry': '2',
                      'kafka_flush_timeout': '3',
                      'kafka_close_timeout': '3'})
    def test_send_to_csv_data_topic(self):
        config.init()

        n = randint(1, 1001)
        key = str.format('key-test-{}', n)
        data = str.format('data-test-{}', n)

        engine = kafka_engine.KafkaEngine()
        engine.send_to_csv_data_topic(key.encode(), data.encode())
        engine.close()
        assert True
