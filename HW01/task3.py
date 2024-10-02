import random

# Randomized Hill Climbing
def hill_climbing(func, start, iterations=100):
    current = start
    current_value = func(current)

    for i in range(iterations):
        next_candidate = current + random.randint(-1, 1)
        next_value = func(next_candidate)

        if next_value > current_value:
            current = next_candidate
            current_value = next_value

    return current, current_value

# Example Function: Maximization
def func_maximization(x):
    return -x**2 + 5

# Test Hill Climbing
start_point = 0
iterations = 100
best_x, best_value = hill_climbing(func_maximization, start_point, iterations)

print("Best X:", best_x)
print("Best Value:", best_value)
