import unittest
import csv


class TestAdjacencyMatrix(unittest.TestCase):

    def setup(self):
        pass

    def create_csv(self, file, table):
        with open('eggs.csv', 'wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow()

if __name__ == '__main__':
    unittest.main()
