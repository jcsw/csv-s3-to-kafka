import csv


class CsvEngine:
    def __init__(self, file):
        self.csv_data = csv.reader(file)

    def process_csv(self, f):
        headers = next(self.csv_data)
        print('headers:{}'.format(headers))

        count = 0
        for line in self.csv_data:
            count += 1
            f(line)

        return count
