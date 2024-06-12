import numpy as np
import heapq
from ManhattanDistance import ManhattanDistance
from Node import Node

def reduce_matrix(matrix):
    row_reduction = np.min(matrix, axis=1)
    row_reduction[row_reduction == np.inf] = 0
    reduced_matrix = matrix - row_reduction[:, np.newaxis]

    col_reduction = np.min(reduced_matrix, axis=0)
    col_reduction[col_reduction == np.inf] = 0
    reduced_matrix = reduced_matrix - col_reduction

    cost = np.sum(row_reduction) + np.sum(col_reduction)
    return reduced_matrix, cost

def calculate_cost(matrix, path):
    cost = 0
    for i in range(len(path) - 1):
        cost += matrix[path[i], path[i+1]]
    return cost

def branch_and_bound(matrix, start):
    n = len(matrix)
    initial_matrix, cost = reduce_matrix(np.copy(matrix))
    root = Node(0, [start], cost, initial_matrix)
    pq = [root]

    best_cost = np.inf
    best_path = None
    it = 1
    while pq:
        current = heapq.heappop(pq)

        print(f"\nIterasi ke: {it}")
        print(f"Current node path: {current.path}")
        print(f"Reduced cost matrix: \n{current.reduced_matrix}")
        print(f"Cost: {current.cost}")
        input("")
        it +=1
        if current.level == n - 1:
            final_cost = calculate_cost(matrix, current.path + [start])
            if final_cost < best_cost:
                best_cost = final_cost
                best_path = current.path + [start]
            pq = [node for node in pq if node.cost <= best_cost]
            heapq.heapify(pq)
            for node in pq:
                print(f"Expanded node path: {node.path} - Cost: {node.cost}")
            continue

        
        for i in range(n):
            if i not in current.path:
                new_path = current.path + [i]
                new_matrix = np.copy(current.reduced_matrix)

                for j in range(n):
                    new_matrix[current.path[-1], j] = np.inf
                    new_matrix[j, i] = np.inf
                new_matrix[i, start] = np.inf

                reduced_matrix, additional_cost = reduce_matrix(new_matrix)
                new_cost = current.cost + current.reduced_matrix[current.path[-1], i] + additional_cost

                if new_cost < best_cost:
                    child_node = Node(current.level + 1, new_path, new_cost, reduced_matrix)
                    heapq.heappush(pq, child_node)
        
        for node in pq:
            print(f"Expanded node path: {node.path} - Cost: {node.cost}")
        input("Enter to continue")
    return best_path, best_cost

if __name__ == "__main__":
    points = [(5, 0), (8, 2), (0, 4), (4, 5), (3, 7), (10, 10)]

    distance_matrix = ManhattanDistance.calculate_distance_matrix(points)
    ManhattanDistance.display_table(distance_matrix)
    for i in range(len(points)):
        distance_matrix[i][i] = np.inf

    best_path, best_cost = branch_and_bound(np.array(distance_matrix), 0)
    print(f"Best path: {best_path}")
    print(f"Best cost: {best_cost}")