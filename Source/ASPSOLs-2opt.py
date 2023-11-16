# import FPA
import time
import ACO
import pso
import ReadDistanceMatrix
import functions
# Đường dẫn đến tệp chứa dữ liệu
file_path = 'TSP-02-Coordinates.txt'
# file_path = 'TSP-01.txt'
# file_path = 'TSP-02.txt'

# Tạo ma trận khoảng cách
distance_matrix = ReadDistanceMatrix.readDistanceMatrix(file_path)
distance_matrix = functions.replace_values_zero(distance_matrix)
distance_matrix = functions.replace_list(distance_matrix)
print(f'Hiện tại có tổng cộng {len(distance_matrix)} thành phố trong tour du lịch.')
print(f'Vui lòng nhập thành phố bạn muốn bắt đầu(Từ 1 đến {len(distance_matrix)}).')
initial = int(input("Nhập thành phố bạn muốn bắt đầu: "))
print('---------------------------------------------------------')
print('Đang khởi tạo đường đi.........')
# Bắt đầu đo thời gian
start_time = time.time()
# Para cho ACO
parameters = {
    'ants': 10,
    'iterations': 15,
    'alpha': 1,
    'beta': 2,
    'decay': 0.05,
    'local_search': True,
    'verbose': True
}
# Chạy đoạn code

pso.particle_swarm_optimization(swarm_size=3, min_values=[0, 0, 0], max_values=[5, 5, 5], iterations=5, decay=0,
                                 w=0.9, c1=2, c2=2,initial=initial, distance_matrix=distance_matrix,
                                  target_function=ACO.ant_colony_optimization)
# print(f'Tour du lịch: {route}, Tổng khoảng cách: {distance}')

# Kết thúc đo thời gian
end_time = time.time()

# Tính thời gian chạy
running_time = end_time - start_time

print(f'Thời gian chạy: {running_time:.2f} giây')
