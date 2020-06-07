import os
import unittest
import csv
from pathlib import Path

from server.adjacencyMatrix import AdjacencyMatrix


class TestAdjacencyMatrix(unittest.TestCase):

    def setUp(self):
        self.file_path = Path.home() / Path('temp.csv')

    def test_adjacent_and(self):
        table = [
            ['', 'Jen', 'Conor'],
            ['Jen', 0, 1],
            ['Conor', 1, 0]
        ]
        self.create_csv(table)
        adjmat = AdjacencyMatrix(self.file_path)
        self.assertTrue(adjmat.open)
        actual = adjmat.is_adjacent('Conor', 'Jen')
        self.assertTrue(actual)

    def test_adjacent_or(self):
        table = [
            ['', 'Jen', 'Conor'],
            ['Jen', 0, 0],
            ['Conor', 1, 0]
        ]
        self.create_csv(table)
        adjmat = AdjacencyMatrix(self.file_path)
        self.assertTrue(adjmat.open)
        actual = adjmat.is_adjacent('Conor', 'Jen')
        self.assertTrue(actual)

    def test_adjacent_empty(self):
        table = [
            ['', 'Jen', 'Conor'],
            ['Jen', '', ''],
            ['Conor', 1, '']
        ]
        self.create_csv(table)
        adjmat = AdjacencyMatrix(self.file_path)
        self.assertTrue(adjmat.open)
        actual = adjmat.is_adjacent('Conor', 'Jen')
        self.assertTrue(actual)

    def rm(self):
        os.remove(self.file_path)

    def create_csv(self, table):
        with open(self.file_path, "w+", encoding="utf-8-sig", newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', skipinitialspace=True)
            writer.writerows(table)

if __name__ == '__main__':
    unittest.main()
