# Required Libraries
import pandas as pd

import distance

coordinates = pd.read_csv('TSP-02-Coordinates.txt', sep='\t')
coordinates = coordinates.values
# Obtaining the Distance Matrix
distance_matrix = distance.build_distance_matrix(coordinates)
# ACO - Parameters
parameters = {
    'ants': 15,
    'iterations': 100,
    'alpha': 1,
    'beta': 2,
    'decay': 0.05,
    'local_search': True,
    'verbose': True
}

# ACO - Algorithm
# route, distance = ACO.ant_colony_optimization(distance_matrix, **parameters)
