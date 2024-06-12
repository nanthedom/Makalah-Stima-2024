from ManhattanDistance import ManhattanDistance

def tsp_greedy(matrix):
    n = len(matrix)
    visited = [False] * n
    tour = []
    
    current_node = 0
    visited[current_node] = True
    tour.append(current_node)
    
    cost = 0
    for _ in range(n - 1):
        nearest_node = None
        nearest_distance = float('inf')
        for next_node in range(n):
            if not visited[next_node] and matrix[current_node][next_node] < nearest_distance:
                nearest_distance = matrix[current_node][next_node]
                nearest_node = next_node
                cost += nearest_distance
        current_node = nearest_node
        visited[current_node] = True
        tour.append(current_node)
        print(f"path: {tour} - cost: {cost}")
        input()
    tour.append(tour[0])
    
    return tour, cost

if __name__ == "__main__":
    points = [(5, 0), (8, 2), (0, 4), (4, 5), (3, 7), (10, 10)]

    distance_matrix = ManhattanDistance.calculate_distance_matrix(points)
    ManhattanDistance.display_table(distance_matrix)

    tour, cost = tsp_greedy(distance_matrix)
    print("Rute yang diambil:", tour)
    print("Cost:", cost)
    print()