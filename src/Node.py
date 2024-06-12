class Node:
    def __init__(self, level, path, cost, reduced_matrix):
        self.level = level
        self.path = path
        self.cost = cost
        self.reduced_matrix = reduced_matrix

    def __lt__(self, other):
        return self.cost < other.cost