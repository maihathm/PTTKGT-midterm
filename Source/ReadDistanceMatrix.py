"""
Mã nguồn triển khai đọc dữ liệu đầu vào.
"""

import os
import distance_matrix

def readDistanceMatrix(file_path):
    """
    Đọc một tệp dữ liệu chứa ma trận khoảng cách từ định dạng được chỉ định và trả về ma trận khoảng cách.

    Args:
        file_path (str): Đường dẫn đến tệp dữ liệu chứa ma trận khoảng cách.

    Returns:
        list of list: Ma trận khoảng cách giữa các điểm trong dữ liệu.
          - Mỗi dòng của ma trận chứa các giá trị khoảng cách từ một điểm đến tất cả các điểm còn lại.
          - Dữ liệu được đọc từ tệp và chuyển thành ma trận.

    Raises:
        FileNotFoundError: Nếu tệp không tồn tại.
    """
    # Kiểm tra xem tệp tồn tại
    if os.path.exists(file_path):
        # Mở tệp để đọc
        with open(file_path, 'r') as file:
            # Đọc dữ liệu từ tệp và tách thành các dòng
            lines = file.readlines()

            # Loại bỏ dòng đầu tiên (tiêu đề, nếu có)
            lines = lines[1:]

            # Khởi tạo danh sách để lưu dữ liệu
            data = {}

            # Lặp qua từng dòng và tách dữ liệu x và y bằng dấu tab
            i = 0
            for line in lines:
                x, y = map(float, line.strip().split('\t'))
                data[i] = (x, y)
                i += 1
        return distance_matrix.build_distance_matrix(data)
    else:
        print(f'Tệp {file_path} không tồn tại.')
