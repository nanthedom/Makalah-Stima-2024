class ManhattanDistance:
    @staticmethod
    def display_table(matrix):
        n = len(matrix)
        print("\n+-------+" + ("--------" * (n + 1)) + "+")
        print("|   No\t|", end="\t")
        for i in range(n):
            if i == 0:
                print("BASE", end="\t")
            else:
                print(f"{i}", end="\t")
        print(" |\n+-------+" + ("--------" * (n + 1)) + "+")
        j = 0
        for row in matrix:
            if (j == 0):
                print("|  BASE\t|", end="\t")
            else:
                print(f"|   {j}\t|", end="\t")
            j += 1
            print(f"\t".join(map(str, row)), end="\t |\n")
            print("|\t|" + ("\t" * (n + 1)) + " |")
        print("+-------+" + ("--------" * (n + 1)) + "+")
        print()

    @staticmethod
    def calculate_distance(point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    @staticmethod
    def calculate_distance_matrix(points):
        n = len(points)
        distance_matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                distance_matrix[i][j] = ManhattanDistance.calculate_distance(points[i], points[j])
        return distance_matrix

if __name__ == "__main__":
    points = [(5, 0), (8, 2), (0, 4), (4, 5), (3, 7), (10, 10)]
    distance_matrix = ManhattanDistance.calculate_distance_matrix(points)
    ManhattanDistance.display_table(distance_matrix)