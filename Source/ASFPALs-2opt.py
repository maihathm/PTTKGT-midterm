def fitness_function(alpha=1, beta=2, decay=0.05, Best_Known_Solution=None, distance_matrix=None, route=[],
                     attractiveness_matrix=None):
    """
    Calculate the fitness value for a given route in the FPA algorithm.

    Args:
        alpha (float): Alpha parameter for balancing pheromone and heuristic information.
        beta (float): Beta parameter for balancing pheromone and heuristic information.
        decay (float): Decay rate for pheromone evaporation.
        Best_Known_Solution (float): The best known solution value if available.
        distance_matrix (list of lists): Matrix of distances between cities.
        route (list): A list representing the sequence of cities to visit.
        attractiveness_matrix (list of lists): Matrix of attractiveness values.

    Returns:
        The fitness value of the route.
    """
    total_distance = 0

    for i in range(len(route) - 1):
        from_city = route[i] - 1  # Adjust to 0-based index
        to_city = route[i + 1] - 1  # Adjust to 0-based index
        total_distance += distance_matrix[from_city][to_city] * (
                alpha * attractiveness_matrix[from_city][to_city] + beta)

    # Calculate the fitness value based on the total distance
    fitness_value = total_distance

    if Best_Known_Solution is not None:
        # Adjust the fitness value based on the best known solution (if available)
        fitness_value = (1 - decay) * fitness_value + (decay * Best_Known_Solution)

    return fitness_value