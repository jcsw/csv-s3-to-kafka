from unittest import TestCase
from mock import patch

from app import lambda_function


class LambdaFunctionTest(TestCase):

    @patch('app.kafka_engine.KafkaEngine')
    def test_process_file(self, kafka_engine_mock):
        csv_file = open('tests/resource/example.csv', 'r')
        lambda_function.process_file(csv_file)
