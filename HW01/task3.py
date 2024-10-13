import random

# Define the minimization function: f(x) = (x - 3)^2
def minimize_function(x):
    return (x - 3) ** 2

# Define the maximization function: f(x) = -x^2 + 5
def maximize_function(x):
    return -(x ** 2) + 5

# Randomized Hill Climbing Algorithm
def hill_climbing_optimization(objective_fn, start_x, num_iterations=1000, step=1, maximize=False):
    current_solution = start_x
    current_value = objective_fn(current_solution)

    for _ in range(num_iterations):
        # Generate a neighbor by modifying the current solution slightly
        neighbor_x = current_solution + random.choice([-step, step])
        neighbor_value = objective_fn(neighbor_x)

        # For maximization, update the current solution if the neighbor is better
        if maximize:
            if neighbor_value > current_value:
                current_solution, current_value = neighbor_x, neighbor_value
        # For minimization, update the current solution if the neighbor is better
        else:
            if neighbor_value < current_value:
                current_solution, current_value = neighbor_x, neighbor_value

    return current_solution, current_value

# Test Minimization
optimal_x, optimal_value = hill_climbing_optimization(minimize_function, start_x=0, maximize=False)
print(f"Optimal solution for minimization: x={optimal_x}, Value={optimal_value}")

# Test Maximization
optimal_x, optimal_value = hill_climbing_optimization(maximize_function, start_x=0, maximize=True)
print(f"Optimal solution for maximization: x={optimal_x}, Value={optimal_value}")


# Randomized Hill Climbing for resource allocation
def calculate_benefit(solution, project_list):
    return sum(project['benefit'] for idx, project in enumerate(project_list) if solution[idx] == 1)

def calculate_time(solution, project_list):
    return sum(project['est_time'] for idx, project in enumerate(project_list) if solution[idx] == 1)

# Feasibility check to ensure we stay within the resource constraints
def check_feasibility(solution, project_list, available_resources):
    total_resources = sum(project['resource'] for idx, project in enumerate(project_list) if solution[idx] == 1)
    return total_resources <= available_resources

# Randomized Hill Climbing for project selection
def hill_climbing_project_selection(project_list, available_resources, objective_fn, maximize=True):
    # Initialize random solution
    current_solution = [random.randint(0, 1) for _ in range(len(project_list))]

    # Ensure the solution fits the resource constraints
    while not check_feasibility(current_solution, project_list, available_resources):
        current_solution = [random.randint(0, 1) for _ in range(len(project_list))]

    current_value = objective_fn(current_solution, project_list)

    for _ in range(1000):
        # Create a neighbor solution by flipping a project choice
        neighbor_solution = current_solution[:]
        project_idx = random.randint(0, len(project_list) - 1)
        neighbor_solution[project_idx] = 1 - neighbor_solution[project_idx]

        # Check feasibility of the new solution
        if check_feasibility(neighbor_solution, project_list, available_resources):
            neighbor_value = objective_fn(neighbor_solution, project_list)

            # Update if the neighbor solution improves the objective
            if (maximize and neighbor_value > current_value) or (not maximize and neighbor_value < current_value):
                current_solution, current_value = neighbor_solution, neighbor_value

    return current_solution, current_value

# Test case 1: Maximize benefit
projects_1 = [
    {'resource': 20, 'benefit': 40},
    {'resource': 30, 'benefit': 50},
    {'resource': 25, 'benefit': 30},
    {'resource': 15, 'benefit': 25}
]
resources_available = 100
solution, value = hill_climbing_project_selection(projects_1, resources_available, calculate_benefit, maximize=True)
print(f"Maximizing Benefit - Solution: {solution}, Total Benefit: {value}")

# Test case 2: Minimize time
projects_2 = [
    {'resource': 10, 'est_time': 15},
    {'resource': 40, 'est_time': 60},
    {'resource': 20, 'est_time': 30},
    {'resource': 25, 'est_time': 35},
    {'resource': 5, 'est_time': 10}
]
solution, value = hill_climbing_project_selection(projects_2, resources_available, calculate_time, maximize=False)
print(f"Minimizing Time - Solution: {solution}, Total Time: {value}")

# Test case 3: Maximize benefit
projects_3 = [
    {'resource': 50, 'benefit': 80},
    {'resource': 30, 'benefit': 45},
    {'resource': 15, 'benefit': 20},
    {'resource': 25, 'benefit': 35}
]
solution, value = hill_climbing_project_selection(projects_3, resources_available, calculate_benefit, maximize=True)
print(f"Maximizing Benefit - Solution: {solution}, Total Benefit: {value}")
