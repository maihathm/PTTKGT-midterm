"""
Mã nguồn này dùng để hỗ trợ việc tính toán một số chức năng của list, ma trận, ...
"""

def sum_list(list):
    """
    Tính tổng của tất cả các phần tử trong danh sách lồng nhau.

    Args:
        lst (list): Danh sách lồng nhau chứa các số nguyên hoặc số thực.

    Returns:
        float or int: Tổng của tất cả các phần tử trong danh sách.
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
    """
    Tạo ma trận trống với kích thước `(rows, cols)`.

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
    """
    Nhân ma trận với một số vô hướng

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

