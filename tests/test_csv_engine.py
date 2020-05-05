from unittest.mock import Mock

from app import csv_engine


def test_load_csv():
    csv_file = open('tests/resource/example.csv', 'r')
    f = Mock()

    engine = csv_engine.CsvEngine(csv_file)
    count = engine.process_csv(f)

    assert 2000 == count
    assert 2000 == f.call_count

