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

