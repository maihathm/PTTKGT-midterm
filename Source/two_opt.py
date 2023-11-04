# Function: Tour Distance
import copy


def distance_calc(distance_matrix, city_tour):
    distance = 0
    for k in range(0, len(city_tour[0]) - 1):
        m = k + 1
        city_k = city_tour[0][k]
        city_m = city_tour[0][m]
        distance = distance + distance_matrix[city_k - 1][city_m - 1]
    return distance


# Function: 2_opt
def local_search_2_opt(distance_matrix, city_tour, recursive_seeding=-1):
    if (recursive_seeding < 0):
        count = -2
    else:
        count = 0
    city_list = copy.deepcopy(city_tour)
    distance = city_list[1] * 2
    while (count < recursive_seeding):
        best_route = copy.deepcopy(city_list)
        seed = copy.deepcopy(city_list)
        for i in range(0, len(city_list[0]) - 2):
            for j in range(i + 1, len(city_list[0]) - 1):
                best_route[0][i:j + 1] = list(reversed(best_route[0][i:j + 1]))
                best_route[0][-1] = best_route[0][0]
                best_route[1] = distance_calc(distance_matrix, best_route)
                if (city_list[1] > best_route[1]):
                    city_list = copy.deepcopy(best_route)
                best_route = copy.deepcopy(seed)
        count = count + 1
        if (distance > city_list[1] and recursive_seeding < 0):
            distance = city_list[1]
            count = -2
            recursive_seeding = -1
        elif (city_list[1] >= distance and recursive_seeding < 0):
            count = -1
            recursive_seeding = -2
    return city_list[0], city_list[1]
