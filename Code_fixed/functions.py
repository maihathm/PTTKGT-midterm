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
    result = []
    for row in matrix:
        new_row = [element * scalar for element in row]
        result.append(new_row)
    return result

