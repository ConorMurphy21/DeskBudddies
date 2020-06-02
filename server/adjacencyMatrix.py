import csv


class AdjacencyMatrix:

    def __init__(self, directory):
        self.directory = directory
        self.matrix = {}
        with open(directory, "r", encoding="utf-8-sig") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
            for row in spamreader:
                adjacencies = {}
                for uid in row:
                    if uid != row[0] and uid != '':
                            adjacencies[uid] = 1

                self.matrix[row[0]] = adjacencies

    def is_adjacent(self, a, b) -> bool:
        return self._is_adjacent(a, b) or self._is_adjacent(b, a)

    def _is_adjacent(self, a, b) -> bool:
        is_adj = 0
        is_adj = self.matrix[a][b]
        return is_adj
