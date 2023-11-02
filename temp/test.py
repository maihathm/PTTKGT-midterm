import FPA
import distance
import pandas as pd
import ACO

coordinates = pd.read_csv('TSP-02-Coordinates.txt', sep = '\t')
coordinates = coordinates.values

distance_matrix = distance.build_distance_matrix(coordinates)
print(distance_matrix)
parameters = {
              'ants': 15,
              'iterations': 100,
              'alpha':1,
              'beta':2,
              'decay':0.05,
              'local_search': True,
              'verbose': True
             }

route, distance = ACO.ant_colony_optimization(distance_matrix, **parameters)

FPA.flower_pollination_algorithm(flowers = 25, min_values = [-5,-5], max_values = [5,5], iterations = 500, gama = 0.1, lamb = 1.5, p = 0.8, target_function = ACO.ant_colony_optimization(distance_matrix, **parameters))