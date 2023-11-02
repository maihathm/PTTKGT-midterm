import ACO
import test
import functions

city_tour = [[28, 52, 13, 27, 33, 51, 9, 10, 19, 45, 18, 20, 17, 1, 16, 41, 8, 22, 3, 50, 5, 46, 35, 37, 49, 43, 40, 39, 24, 44, 4, 26, 47, 38, 48, 32, 6, 15, 34, 31, 36, 23, 30, 42, 2, 7, 21, 29, 25, 12, 14, 11, 28], 16506.708922438545]

# Oke
distance_calc = ACO.distance_calc(test.distance_matrix, city_tour)
# print(distance_calc)

# Oke
local_search_2_opt = ACO.local_search_2_opt(test.distance_matrix, city_tour, recursive_seeding = -1)
# print(local_search_2_opt)

# Oke
attractiveness = ACO.attractiveness(test.distance_matrix)
# print(attractiveness)

# Oke
h = attractiveness
thau = functions.create_empty_matrix_ones(len(test.distance_matrix), len(test.distance_matrix))
i = 2
alpha = 1
beta = 2
city_list = [47, 22, 7, 41, 25, 15, 24, 2, 39, 10, 9, 13, 11, 12, 52, 6, 50, 19, 45, 4, 21, 37, 1, 20, 5, 16, 28, 26, 51, 3, 46, 18, 49, 43, 35, 34, 44, 40, 48, 36, 38, 8, 33, 31, 30, 32, 23, 29, 27, 42, 17]
city_probability = ACO.city_probability(h, thau, city = i, alpha = alpha, beta = beta, city_list = city_list)
# print(city_probability)

# Hàm này đang lỗi(Lỗi j chưa tìm ra)
city_selection = ACO.city_selection(city_probability, city_list)
print(city_selection)

# Oke
update_thau = ACO.update_thau(test.distance_matrix, thau, city_list)
# print(update_thau)
total = 0
for sublist in update_thau:
    for item in sublist:
        total += item
# print(total)

# Do hàm city_selection sai kéo theo hàm này chưa check được
ants = 5
local_search = True
full_list = list(range(1, len(test.distance_matrix) + 1))
ants_path = ACO.ants_path(test.distance_matrix, h, thau, alpha, beta, full_list, ants, local_search)
# print(ants_path)

# ant_colony_optimization = ACO.ant_colony_optimization(test.distance_matrix, ants = 5, iterations = 50, alpha = 1, beta = 2, decay = 0.05, local_search = True, verbose = True)
# print(ant_colony_optimization)
