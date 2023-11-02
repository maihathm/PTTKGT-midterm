# import numpy  as np
# # Function: Build Distance Matrix
# def build_distance_matrix(coordinates):
#    a = coordinates
#    b = a.reshape(np.prod(a.shape[:-1]), 1, a.shape[-1])
#    return np.sqrt(np.einsum('ijk,ijk->ij',  b - a,  b - a)).squeeze()

# Function: Build Distance Matrix
import math

# Function: Build Distance Matrix
def build_distance_matrix(coordinates):
    n = len(coordinates)
    distance_matrix = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j:
                distance = math.sqrt(sum((a - b) ** 2 for a, b in zip(coordinates[i], coordinates[j])))
                distance_matrix[i][j] = distance

    return distance_matrix
