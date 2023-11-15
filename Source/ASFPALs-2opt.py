# import FPA
import time
import ACO
import FPA
import ReadDistanceMatrix
import functions
# Đường dẫn đến tệp chứa dữ liệu
file_path = 'TSP-02-Coordinates.txt'
# file_path = 'TSP-01.txt'
# file_path = 'TSP-02.txt'

# Tạo ma trận khoảng cách
distance_matrix = ReadDistanceMatrix.readDistanceMatrix("TSP-02.txt")
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

FPA.flower_pollination_algorithms(flowers=5, min_values=[0.001, 0.001, 0.001],
                                  max_values=[5, 5, 5], iteration=5,
                                  gamma=0.1, lamb=1.5, p=0.8,
                                  initial=initial, distance_matrix=distance_matrix,
                                  function=ACO.ant_colony_optimization)
# print(f'Tour du lịch: {route}, Tổng khoảng cách: {distance}')

# Kết thúc đo thời gian
end_time = time.time()

# Tính thời gian chạy
running_time = end_time - start_time

print(f'Thời gian chạy: {running_time:.2f} giây')
