from contextvars import ContextVar
from os import environ

kafka_server = ContextVar("kafka_server")
kafka_producer_timeout = ContextVar("kafka_producer_timeout")
kafka_producer_retry = ContextVar("kafka_producer_retry")
kafka_flush_timeout = ContextVar("kafka_flush_timeout")
kafka_close_timeout = ContextVar("kafka_close_timeout")


def init():
    kafka_server.set(str(environ.get('kafka_server')))
    kafka_producer_timeout.set(int(environ.get('kafka_producer_timeout')))
    kafka_producer_retry.set(int(environ.get('kafka_producer_retry')))
    kafka_flush_timeout.set(int(environ.get('kafka_flush_timeout')))
    kafka_close_timeout.set(int(environ.get('kafka_close_timeout')))
