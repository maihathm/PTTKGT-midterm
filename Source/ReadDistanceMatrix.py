# import FPA
import os

import distance_matrix


# Đường dẫn đến tệp chứa dữ liệu
# file_path = 'TSP-02-Coordinates.txt'
# file_path = 'TSP-01.txt'
def readDistanceMatrix(file_path):
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
