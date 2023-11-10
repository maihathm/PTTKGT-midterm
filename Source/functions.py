import random
'''
File functions chứa một số hàm hỗ trợ cho việc tính toán file ACO
'''


def sum_list(list): # Đầu vào là một list các phần tử
  total = 0
  for sublist in list:
    for item in sublist:
      total += item
  return total # Trả về tổng các phần tử có trong list

def create_empty_matrix(rows, cols):
  """Tạo ma trận trống với kích thước `(rows, cols)`.

  Args:
    rows: Số hàng của ma trận.
    cols: Số cột của ma trận.

  Returns:
    Ma trận trống với kích thước `(rows, cols)`.
  """

  matrix = []
  for row in range(rows):
    matrix.append([])
    for col in range(cols):
      matrix[row].append(0)
  return matrix 

def create_empty_matrix_ones(rows, cols):
  """Tạo ma trận trống với kích thước `(rows, cols)`.

  Args:
    rows: Số hàng của ma trận.
    cols: Số cột của ma trận.

  Returns:
    Ma trận trống với kích thước `(rows, cols)`.
  """

  matrix = []
  for row in range(rows):
    matrix.append([])
    for col in range(cols):
      matrix[row].append(1)
  return matrix
  
def matrix_multiply(matrix, scalar):
  """Nhân ma trận với một số vô hướng 

  Args:
    matrix: Ma trận đầu vào.
    scalar: Một số.

  Returns:
    Trả về một ma trận mới với tất cả các phần tử được nhân với số vô hướng.
  """
  result = []
  for row in matrix:
    new_row = [element * scalar for element in row]
    result.append(new_row)
  return result

def replace_list(list): # Đầu vào là một list các phần tử
  for i in range(len(list)):
    for j in range(len(list[i])):
        if list[i][j] == 0.0:
            list[i][j] = 999999999999.0
  return list

# Đang test
import random

list = [[5,4,3,5],[4,0,6,4],[3,6,0,7],[5,4,10,0]]

number_of_elements = len(list) * len(list[0])
number_of_zeros = int(number_of_elements * 0.1)

for i in range(number_of_zeros):
    random_number = random.random()
    if random_number < 0.1:
        random_index = random.choice(range(number_of_elements))
        list[random_index // len(list[0])][random_index % len(list[0])] = 0

print(list)
