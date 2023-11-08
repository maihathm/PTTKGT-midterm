# import FPA
import distance_matrix
import ACO
import os

# Đường dẫn đến tệp chứa dữ liệu
# file_path = 'TSP-02-Coordinates.txt'
# file_path = 'TSP-01.txt'
file_path = 'TSP-02.txt'

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
        i=0
        for line in lines:
            x, y = map(float, line.strip().split('\t'))
            data[i]=(x, y)
            i+=1
else:
    print(f'Tệp {file_path} không tồn tại.')

distance_matrix = distance_matrix.build_distance_matrix(data)

parameters = {
              'ants': 10,
              'iterations': 50,
              'alpha':1,
              'beta':2,
              'decay':0.05,
              'local_search': True,
              'verbose': True
             }

route, distance = ACO.ant_colony_optimization(distance_matrix, **parameters)
print(route, distance)
# FPA.flower_pollination_algorithm(flowers = 25, min_values = [-5,-5], max_values = [5,5], iterations = 500, gama = 0.1, lamb = 1.5, p = 0.8, target_function = ACO.ant_colony_optimization(distance_matrix, **parameters))