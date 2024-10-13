import heapq
import math

# Graph representation with nodes as grid positions and weights as edge costs from the image
graph = {
    (0, 0): {(1, 0): 4, (0, 1): 2},
    (0, 1): {(0, 0): 2, (1, 1): 4, (0, 2): 3},
    (0, 2): {(0, 1): 3, (1, 2): 4, (0, 3): 6},
    (0, 3): {(0, 2): 6, (1, 3): 2, (0, 4): 8},
    (0, 4): {(0, 3): 8, (1, 4): 4},
    
    (1, 0): {(0, 0): 4, (2, 0): 3, (1, 1): 1},
    (1, 1): {(1, 0): 1, (0, 1): 4, (2, 1): 3, (1, 2): 2},
    (1, 2): {(1, 1): 2, (0, 2): 4, (2, 2): 1, (1, 3): 1},
    (1, 3): {(1, 2): 1, (0, 3): 2, (2, 3): 3, (1, 4): 2},
    (1, 4): {(1, 3): 2, (0, 4): 4, (2, 4): 6},
    
    (2, 0): {(1, 0): 3, (3, 0): 9, (2, 1): 3},
    (2, 1): {(2, 0): 3, (1, 1): 3, (3, 1): 2, (2, 2): 1},
    (2, 2): {(2, 1): 1, (1, 2): 1, (3, 2): 7, (2, 3): 3},
    (2, 3): {(2, 2): 3, (1, 3): 3, (3, 3): 2, (2, 4): 5},
    (2, 4): {(2, 3): 5, (1, 4): 6, (3, 4): 5},
    
    (3, 0): {(2, 0): 9, (4, 0): 2, (3, 1): 2},
    (3, 1): {(3, 0): 2, (2, 1): 2, (4, 1): 5, (3, 2): 7},
    (3, 2): {(3, 1): 7, (2, 2): 7, (4, 2): 6, (3, 3): 7},
    (3, 3): {(3, 2): 7, (2, 3): 2, (4, 3): 9, (3, 4): 3},
    (3, 4): {(3, 3): 3, (2, 4): 5, (4, 4): 1},
    
    (4, 0): {(3, 0): 2, (4, 1): 5},
    (4, 1): {(4, 0): 5, (3, 1): 5, (4, 2): 6},
    (4, 2): {(4, 1): 6, (3, 2): 6, (4, 3): 9},
    (4, 3): {(4, 2): 9, (3, 3): 9, (4, 4): 1},
    (4, 4): {(3, 4): 1, (4, 3): 1}
}

# Heuristic function (Euclidean distance)
def heuristic(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# A* Algorithm
def a_star(graph, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_score = {node: float('infinity') for node in graph}
    g_score[start] = 0
    f_score = {node: float('infinity') for node in graph}
    f_score[start] = heuristic(start, goal)

    while open_list:
        current = heapq.heappop(open_list)[1]

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1], g_score[goal]

        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None, float('infinity')

# Define the start and goal nodes
start = (0, 0)
goal = (2, 3)

# Run the A* algorithm
path, travel_time = a_star(graph, start, goal)
print(f"Optimal path: {path}")
print(f"Total travel time: {travel_time}")


import random

# Objective function for minimization: f(x) = (x - 3)^2
def minimization_function(x):
    return (x - 3) ** 2

# Objective function for maximization: f(x) = -x^2 + 5
def maximization_function(x):
    return -(x) ** 2 + 5

# Randomized Hill Climbing Algorithm
def randomized_hill_climbing(objective_function, x_start, iterations=1000, step_size=1, maximize=False):
    current_x = x_start
    current_value = objective_function(current_x)

    for _ in range(iterations):
        # Generate a neighboring solution by making a small random change
        neighbor_x = current_x + random.choice([-step_size, step_size])
        neighbor_value = objective_function(neighbor_x)

        # For maximization, move if the neighbor's value is higher
        if maximize:
            if neighbor_value > current_value:  # Maximization condition
                current_x = neighbor_x
                current_value = neighbor_value
        else:
            # For minimization, move if the neighbor's value is lower
            if neighbor_value < current_value:  # Minimization condition
                current_x = neighbor_x
                current_value = neighbor_value

    return current_x, current_value

# Test Minimization Function
optimal_x, optimal_value = randomized_hill_climbing(minimization_function, x_start=0, iterations=1000, maximize=False)
print(f"Optimal x for minimization: {optimal_x}, Function value: {optimal_value}")

# Test Maximization Function
optimal_x, optimal_value = randomized_hill_climbing(maximization_function, x_start=0, iterations=1000, maximize=True)
print(f"Optimal x for maximization: {optimal_x}, Function value: {optimal_value}")
