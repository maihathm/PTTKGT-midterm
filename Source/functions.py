"""
Mã nguồn này dùng để hỗ trợ việc tính toán một số chức năng của list, ma trận, ...
"""

def sum_list(list:list)->float:
    """
    Tính tổng của tất cả các phần tử trong danh sách lồng nhau.

    Args:
        lst : Danh sách lồng nhau chứa các số nguyên hoặc số thực.

    Returns:
        float or int: Tổng của tất cả các phần tử trong danh sách.
    """
    total = 0
    for sublist in list:
        for item in sublist:
            total += item
    return total 


def create_empty_matrix(rows:int, cols:int)->list:
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


def create_empty_matrix_ones(rows:int, cols:int)->list:
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


def matrix_multiply(matrix:list, scalar:float)->list:
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
def find_best_global(positions:list)->list:
    """
    Tìm và trả về phần tử có giá trị cuối cùng (vị trí cuối cùng trong mỗi sublist) lớn nhất trong danh sách.
    
    Parameters:
    - positions: Danh sách chứa các danh sách con, mỗi danh sách con có ít nhất một phần tử.
    
    Returns:
    - Phần tử có giá trị bé nhất trong danh sách.
    """
    if not positions:
        return None  # Trả về None nếu danh sách rỗng

    # Khởi tạo phần tử có giá trị bé nhất
    best_global = positions[0]

    # Duyệt qua danh sách để tìm phần tử bé nhất
    for position in positions:
        if position[-1] < best_global[-1]:
            best_global = position
    
    return best_global
