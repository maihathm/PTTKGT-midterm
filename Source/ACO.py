import copy
import os
import random

import functions
import two_opt

random.seed(10)


# Function: Initial Attractiveness
def attractiveness(distance_matrix):
    h = functions.create_empty_matrix(len(distance_matrix), len(distance_matrix))
    for i in range(0, len(distance_matrix)):
        for j in range(0, len(distance_matrix[i])):
            if (i == j or distance_matrix[i][j] == 0):
                h[i][j] = 0.000001
            else:
                h[i][j] = 1 / distance_matrix[i][j]
    return h


# Function: Probability Matrix
def city_probability(h, thau, city=0, alpha=1, beta=2, city_list=[]):
    num_cities = len(h)
    probability = [[0, 0, 0] for _ in range(num_cities)]
    total_attraction = 0
    for i in range(num_cities):
        total_attraction = sum([probability[i][0] for i in range(0, len(probability))])
        if i + 1 not in city_list:
            attraction = (thau[i][city] ** alpha) * (h[i][city] ** beta)
            probability[i][0] = attraction

    for i in range(num_cities):
        if i + 1 not in city_list and total_attraction != 0:
            temp_total = sum([probability[i][0] for i in range(0, len(probability))])
            probability[i][1] = probability[i][0] / temp_total
        if i == 0:
            probability[i][2] = probability[i][1]
        else:
            probability[i][2] = probability[i][1] + probability[i - 1][2]

    if len(city_list) > 0:
        for i in range(len(city_list)):
            probability[city_list[i] - 1][2] = 0.0

    return probability


# Function: Select Next City
def city_selection(probability_matrix, city_list=[]):
    random = int.from_bytes(os.urandom(8), byteorder='big') / ((1 << 64) - 1)
    city = 0
    for i in range(0, len(probability_matrix)):
        if (random <= probability_matrix[i][2] and i + 1 not in city_list):
            city = i + 1
            break
    return city


# Function: Update Thau
def update_thau(distance_matrix, thau, city_list=[]):
    distance = 0
    city_tour = copy.deepcopy(city_list)
    random_number = 0
    city_tour = random_number, *city_tour, random_number
    for i in range(0, len(city_list) - 1):
        j = i + 1
        distance = distance + distance_matrix[city_tour.index(city_list[i]) - 1][city_tour.index(city_list[j]) - 1]
    pheromone = 1
    for i in range(0, len(city_list) - 1):
        j = i + 1
        m = city_tour.index(city_list[i]) - 1
        n = city_tour.index(city_list[j]) - 1
        thau[m][n] = thau[m][n] + pheromone
    return thau


# Function: Ants City List
def ants_path(distance_matrix, h, thau, alpha, beta, full_list, ants, local_search):
    distance = functions.sum_list(distance_matrix)
    best_city_list = []
    best_path_distance = []
    for ant in range(0, ants):
        city_list = []
        initial = random.randrange(1, len(distance_matrix))
        city_list.append(initial)
        for i in range(0, len(distance_matrix) - 1):
            probability = city_probability(h, thau, city=i, alpha=alpha, beta=beta, city_list=city_list)
            path_point = city_selection(probability, city_list=city_list)
            if (path_point == 0):
                path_point = [value for value in full_list if value not in city_list][0]
            city_list.append(path_point)
        city_list.append(city_list[0])
        path_distance = 0
        for i in range(0, len(city_list) - 1):
            j = i + 1
            path_distance = path_distance + distance_matrix[(city_list[i]) - 1][(city_list[j]) - 1]
        if (distance > path_distance):
            best_city_list = copy.deepcopy(city_list)
            best_path_distance = path_distance
            distance = path_distance
    best_route = copy.deepcopy([best_city_list])
    best_route.append(best_path_distance)
    if (local_search == True):
        best_city_list, best_path_distance = two_opt.local_search_2_opt(distance_matrix, city_tour=best_route,
                                                                        recursive_seeding=-1)
    thau = update_thau(distance_matrix, thau, city_list=best_city_list)

    return best_city_list, best_path_distance, thau


# ACO Function
def ant_colony_optimization(distance_matrix, ants=5, iterations=50, alpha=1, beta=2, decay=0.05, local_search=True,
                            verbose=True):
    count = 0
    best_route = []
    full_list = list(range(1, len(distance_matrix) + 1))
    distance = functions.sum_list(distance_matrix)
    h = attractiveness(distance_matrix)
    thau = functions.create_empty_matrix_ones(len(distance_matrix), len(distance_matrix))
    while (count <= iterations):
        if (verbose == True and count > 0):
            print('Iteration = ', count, 'Distance = ', round(best_route[1], 2))
            # print(best_route)     
        city_list, path_distance, thau = ants_path(distance_matrix, h, thau, alpha, beta, full_list, ants, local_search)
        thau = functions.matrix_multiply(thau, 1 - decay)
        if (distance > path_distance):
            best_route = copy.deepcopy([city_list])
            best_route.append(path_distance)
            distance = best_route[1]
        count = count + 1
    route, distance = best_route
    return route, distance
