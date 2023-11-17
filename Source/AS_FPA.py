# import FPA
import random
import time

import ACO
import FPA
import ReadDistanceMatrix


def AS_FPA(MaxIteration, MaxFlower, min_values, max_values, initial, distance_matrix, BKS=7566):
    """

    :param MaxIteration:
    :param MaxFlower:
    :param min_values:
    :param max_values:
    :param initial:
    :param distance_matrix:
    :param BKS:

    :return:
    """

    # Initialization of the Supervising heuristic parameters (alpha, beta, decay)

    # Tạo alpha, beta, decay ban đầu
    alpha = random.uniform(min_values[0], max_values[0])
    beta = random.uniform(min_values[1], max_values[1])
    decay = random.uniform(min_values[2], max_values[2])

    # Initialization of Problem Solving Heuristic (ACO)
    route = []
    distance = 99999999999999
    print("init position FPA")
    fpa_position = FPA.init_population(
        N=MaxFlower,
        min_val=min_values,
        max_val=max_values,
        function=ACO.ant_colony_optimization,
        initial=initial,
        distance_matrix=distance_matrix
    )

    for i in range(0, MaxIteration):
        # If reach BKS, stop
        if distance == BKS:
            break

        # # Initialization of Problem Solving Heuristic (ACO)

        # FPA processing
        print(f'Chạy FPA lần thứ {i + 1}')
        fpa = FPA.flower_pollination_algorithms(
            position=fpa_position,
            # flowers=10, # Số lượng bông hoa
            min_values=min_values,
            max_values=max_values,
            iteration=5,
            gamma=0.1,
            lamb=1.5,
            p=0.8,
            initial=initial,
            distance_matrix=distance_matrix,
            function=ACO.ant_colony_optimization,  # TSP tour length trả về bới ACO,
            distance=distance  # Khoảng cách tốt nhất hiện tại
        )
        # Set ACO (parameters) = Pollen_Position(s)
        alpha, beta, decay = fpa[0:len(min_values)]
        # Lunch ACO() instances
        print(f"Chạy ACO với alpha = {alpha}, beta = {beta}, decay = {decay}")
        route_aco, distance_aco = ACO.ant_colony_optimization(
            ants=10,
            iterations=30,
            alpha=alpha,
            beta=beta,
            decay=decay,
            local_search=True,
            verbose=True,
            initial=initial,
            distance_matrix=distance_matrix
        )
        if distance_aco < distance:
            distance = distance_aco
            route = route_aco
        print(f'Khoảng cách tốt nhất hiện tại: {distance}')
    print(f'Tour: {route}, Tổng khoảng cách: {distance}')
    return route, distance


# Đường dẫn đến tệp chứa dữ liệu
file_path = 'TSP-02-Coordinates.txt'

# Tạo ma trận khoảng cách
distance_matrix = ReadDistanceMatrix.readDistanceMatrix(file_path)
# distance_matrix = functions.replace_values_zero(distance_matrix)
# distance_matrix = functions.replace_list(distance_matrix)
print(f'Hiện tại có tổng cộng {len(distance_matrix)} thành phố trong tour du lịch.')
print(f'Vui lòng nhập thành phố bạn muốn bắt đầu(Từ 1 đến {len(distance_matrix)}).')
initial = int(input("Nhập thành phố bạn muốn bắt đầu: "))
print('---------------------------------------------------------')
print('Đang khởi tạo đường đi.........')
# Bắt đầu đo thời gian
start_time = time.time()

as_fpa = AS_FPA(
    distance_matrix=distance_matrix,  # Ma trận khoảng cách
    MaxIteration=15,  # Số lần lặp tối đa để giải TSP
    MaxFlower=5,  # Số lượng bông hoa
    min_values=[0.001, 0.001, 0.001],
    max_values=[5, 5, 5],
    initial=initial
)

# Kết thúc đo thời gian
end_time = time.time()

# Tính thời gian chạy
running_time = end_time - start_time

print(f'Thời gian chạy: {running_time:.2f} giây')
