import numpy  as np
# Function: Build Distance Matrix
def build_distance_matrix(coordinates):
   a = coordinates
   b = a.reshape(np.prod(a.shape[:-1]), 1, a.shape[-1])
   return np.sqrt(np.einsum('ijk,ijk->ij',  b - a,  b - a)).squeeze()

import math

def build_distance_matrix(coordinates):
  """
  Tính ma trận khoảng cách giữa các điểm trong mảng `coordinates`.

  Args:
    coordinates: Mảng 2 chiều chứa tọa độ của các điểm.

  Returns:
    Mảng 2 chiều chứa khoảng cách giữa các điểm.
  """

  n_points = coordinates.shape[0]
  distance_matrix = np.zeros((n_points, n_points))
  for i in range(n_points):
    for j in range(i + 1, n_points):
      distance_matrix[i, j] = math.sqrt(
          sum((coordinates[i] - coordinates[j]) ** 2))
      distance_matrix[j, i] = distance_matrix[i, j]

  return distance_matrix

import math

# # Function: Build Distance Matrix
def build_distance_matrix_fix(coordinates):
    n = len(coordinates)
    distance_matrix = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                distance = math.sqrt(sum((a - b) ** 2 for a, b in zip(coordinates[i], coordinates[j])))
                distance_matrix[i][j] = distance

    return distance_matrix



import pandas as pd
coordinates = pd.read_csv('TSP-02-Coordinates.txt', sep = '\t')
coordinates = coordinates.values

distance_matrix = build_distance_matrix(coordinates)
distance_matrix_fix = build_distance_matrix_fix(coordinates)

print(len(distance_matrix_fix))
print(distance_matrix.shape[0])

def sum_list(list):
  """Tính tổng các phần tử trong list.

  Args:
    list: List cần tính tổng.

  Returns:
    Tổng các phần tử trong list.
  """

  total = 0
  for sublist in list:
    for item in sublist:
      total += item
  return total

print(np.sum(distance_matrix.sum()))
print(sum_list(distance_matrix_fix))

print(distance_matrix[5,5])
print(distance_matrix_fix[5][5])

