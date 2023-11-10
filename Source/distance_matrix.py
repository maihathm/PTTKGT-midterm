import math


def build_distance_matrix(data):
    """Tạo ma trận khoảng cách giữa các điểm trong dữ liệu.

  Args:
    data: Danh sách các điểm, mỗi điểm được biểu diễn bằng một danh sách hai phần tử,
      phần tử đầu tiên là tọa độ x và phần tử thứ hai là tọa độ y.

  Returns:
    Ma trận khoảng cách giữa các điểm trong dữ liệu.
  """
    num_rows = len(data)
    num_columns = len(data)

    matrix = []
    for i in range(num_rows):
        row = []
        for j in range(num_columns):
            row.append(round(math.sqrt((data[i][0] - data[j][0]) ** 2 + (data[i][1] - data[j][1]) ** 2), 2))
        matrix.append(row)

    return matrix
