import copy
import os
import random

import functions
import two_opt

random.seed(10)


# Function: Initial Attractiveness
def attractiveness(distance_matrix):
    """Tính độ hấp dẫn của một ma trận khoảng cách.

  Args:
    distance_matrix: Ma trận khoảng cách giữa các điểm.

  Returns:
    Một ma trận mới, trong đó mỗi phần tử biểu diễn độ hấp dẫn của cạnh tương ứng trong ma trận khoảng cách đầu vào.
  """
    # Tạo một ma trận biểu diễn độ hấp dẫn của từng cạnh
    h = functions.create_empty_matrix(len(distance_matrix), len(distance_matrix))
    # Duyệt qua tất cả các phần tử của ma trận khoảng cách
    for i in range(0, len(distance_matrix)):
        for j in range(0, len(distance_matrix[i])):
            if (i == j or distance_matrix[i][j] == 0):
                h[i][j] = 0.000001
            else:
                h[i][j] = 1 / distance_matrix[i][j]
    return h


# Function: Probability Matrix
def city_probability(h, thau, city=0, alpha=1, beta=2, city_list=[]):
    """
    Tính toán xác suất tham quan của mỗi thành phố trong một chuyến du lịch dựa trên ma trận pheromone, ma trận heuristic và thành phố hiện tại.

    Args:
        h: Ma trận heuristic(ma trận hấp dẫn) của các thành phố.
        thau: Ma trận pheromone của các thành phố.
        city: Thành phố hiện tại.
        alpha: Hệ số alpha.
        beta: Hệ số beta.
        city_list: Danh sách các thành phố đã được tham qian
    Returns:
        Một ma trận mới, trong đó mỗi phần tử biểu diễn xác xuất tham quan của mỗi thành phố.
    """
    # Số lượng thành phố
    num_cities = len(h)
    # Tạo ma trận để lưu trữ xác xuất tham quan của mỗi thành phố
    probability = [[0, 0, 0] for _ in range(num_cities)]
    # Biến lưu trữ tổng độ hấp dẫn của tất cả các thành phố
    total_attraction = 0
    # Duyệt qua từng thành phố
    for i in range(num_cities):
        # Tính tổng độ hấp dẫn của các thành phố
        total_attraction = sum([probability[i][0] for i in range(0, len(probability))])
        # Kiểm tra xem thành phố đã được tham qua hay chưa
        if i + 1 not in city_list:
            # Tính độ hấp dẫn của thành phố bằng ma trận pheromone và ma trận hấp dẫn
            attraction = (thau[i][city] ** alpha) * (h[i][city] ** beta)
            # Lưu độ hấp dẫn của thành phố trong ma trận xác xuất
            probability[i][0] = attraction

    for i in range(num_cities):
        if i + 1 not in city_list and total_attraction != 0:
            temp_total = sum([probability[i][0] for i in range(0, len(probability))])
            probability[i][1] = probability[i][0] / temp_total
        if i == 0:
            probability[i][2] = probability[i][1]
        else:
            probability[i][2] = probability[i][1] + probability[i - 1][2]

    if len(city_list) > 0:
        for i in range(len(city_list)):
            probability[city_list[i] - 1][2] = 0.0
    # Trả về ma trận xác xuất
    return probability


# Function: Select Next City
def city_selection(probability_matrix, city_list=[]):
    """
    Lựa chọn một thành phố để tham quan tiếp theo dựa trên ma trận xác suất và danh sách các thành phố đã được tham quan.

    Args:
        probability_matrix: Ma trận xác suất của các thành phố.
        city_list: Danh sách các thành phố đã được tham quan.

    Returns:
        Thành phố được lựa chọn để tham quan tiếp theo.

    """
    # Tạo ngẫu nhiên 1 số giữa 0 và 1
    random = int.from_bytes(os.urandom(8), byteorder='big') / ((1 << 64) - 1)
    # Biến lưu trữ thành phố được chọn tiếp theo
    city = 0
    # Duyệt qua các hàng của ma trận xác xuất
    for i in range(0, len(probability_matrix)):
        # Nếu số cho ngẫu nhiên bằng hoặc nhỏ hơn xác xuất tích lũy của của thành phố và thành phố chưa được tham quan trả về thành phố đó
        if (random <= probability_matrix[i][2].real and i + 1 not in city_list):
            city = i + 1
            break
    # Trả về thành phố được chọn
    return city


# Function: Update Thau
def update_thau(distance_matrix, thau, city_list=[]):
    """
    Cập nhật ma trận pheromone sau khi hoàn thành một chuyến tham quan.

    Args:
        distance_matrix: Ma trận khoảng cách giữa các thành phố.
        thau: Ma trận pheromone của các thành phố.
        city_list: Danh sách các thành phố trong chuyến tham quan.

    Returns:
        Ma trận pheromone đã được cập nhật.

    """
    # Biến lưu trữ tổng khoảng cách của chuyến tham quan
    distance = 0
    # Tạo bản sao danh sách các thành phố trong chuyến tham quan
    city_tour = copy.deepcopy(city_list)
    # Thêm thành phố ngẫu nhiên vào đầu và cuối danh sách chuyến tham quan
    # Để đảm bảo luôn có 1 cạnh bất kỳ giữa 2 thành phố
    random_number = 0
    city_tour = random_number, *city_tour, random_number
    # Duyệt qua các cạnh và tính tổng khoảng cách chuyến tham quan
    for i in range(0, len(city_list) - 1):
        j = i + 1
        distance = distance + distance_matrix[city_tour.index(city_list[i]) - 1][city_tour.index(city_list[j]) - 1]
    # Tạo biến pheromone 
    pheromone = 1
    # Duyệt qua các cạnh trong chuyến tham qua và cập nhật pheeromone
    for i in range(0, len(city_list) - 1):
        j = i + 1
        m = city_tour.index(city_list[i]) - 1
        n = city_tour.index(city_list[j]) - 1
        thau[m][n] = thau[m][n] + pheromone
    # Trả về ma trận pheromone đã được cập nhật
    return thau


# Function: Ants City List
def ants_path(initial, distance_matrix, h, thau, alpha, beta, full_list, ants, local_search):
    """
    Tìm đường đi ngắn nhất qua một tập các thành phố bằng thuật toán Optimization của Kiến (ACO).

    Args:
        initial: Vị trí bắt đầu
        distance_matrix: Ma trận khoảng cách giữa các thành phố.
        h: Ma trận heuristic của các thành phố.
        thau: Ma trận pheromone của các thành phố.
        alpha: Hệ số alpha.
        beta: Hệ số beta.
        full_list: Danh sách đầy đủ các thành phố.
        ants: Số lượng ong.
        local_search: Có thực hiện tìm kiếm cục bộ hay không.

    Returns:
        best_city_list: Đường đi tốt nhất được tìm thấy bởi thuật toán.
        best_path_distance: Khoảng cách của đường đi tốt nhất được tìm thấy bởi thuật toán.
        thau: Ma trận pheromone được cập nhật.

    """
    # Biến chứa tổng khoảng cách giữa các thành phố
    distance = functions.sum_list(distance_matrix)
    best_city_list = []
    best_path_distance = []
    # Lặp qua tất cả các con kiến trong đàn
    for ant in range(0, ants):
        city_list = []
        # initial = random.randrange(1, len(distance_matrix)) 
        # initial =  2
        city_list.append(initial)
        # Duyệt qua tất cả các thành phố còn lại
        for i in range(0, len(distance_matrix) - 1):
            # Tính xác xuất tham qua của mỗi thành phố
            probability = city_probability(h, thau, city=i, alpha=alpha, beta=beta, city_list=city_list)
            # Chọn thành phố tiếp theo
            path_point = city_selection(probability, city_list=city_list)
            # Nếu thành phố tiếp theo đã được tham quan
            if (path_point == 0):
                # Chọn thành phố ngẫu nhiên trong các thành phố chưa được tham quan
                path_point = [value for value in full_list if value not in city_list][0]
            # Thêm thành phố tiếp theo vào
            city_list.append(path_point)
        city_list.append(city_list[0])
        path_distance = 0
        # Duyệt qua các thành phố đã tham quan
        for i in range(0, len(city_list) - 1):
            j = i + 1
            # Tính tổng khoảng cách kiến đã đi
            path_distance = path_distance + distance_matrix[(city_list[i]) - 1][(city_list[j]) - 1]
        # So sánh đường đi của kiến với khoảng cách tốt nhất đã được tìm thấy
        if (distance > path_distance):
            best_city_list = copy.deepcopy(city_list)
            best_path_distance = path_distance
            distance = path_distance
    best_route = copy.deepcopy([best_city_list])
    best_route.append(best_path_distance)
    # Sử dụng 2_opt để tiếp tục cải thiện đường đi
    if (local_search == True):
        best_city_list, best_path_distance = two_opt.local_search_2_opt(distance_matrix, city_tour=best_route,
                                                                        recursive_seeding=-1)
    # Cập nhập lại ma trận pheromone 
    thau = update_thau(distance_matrix, thau, city_list=best_city_list)

    # Trả về đường đi tốt nhất, khoảng cách của đường đi, ma trận pheromone
    return best_city_list, best_path_distance, thau


# ACO Function
def ant_colony_optimization(initial, distance_matrix, ants=5, iterations=5, alpha=1, beta=2, decay=0.05,
                            local_search=True,
                            verbose=True):
    """
    Tìm đường đi ngắn nhất qua một tập các thành phố bằng thuật toán Optimization của Kiến (ACO)

    Args:
        initial: Vị trí bắt đầu
        distance_matrix: Ma trận khoảng cách giữa các thành phố
        ants: Số lượng ong trong đàn. (mặc định: 5)
        iterations: Số lần lặp để chạy thuật toán ACO. (mặc định: 50)
        alpha: Hệ số alpha điều khiển tầm quan trọng của các dấu vết pheromone. (mặc định: 1)
        beta: Hệ số beta điều khiển tầm quan trọng của thông tin heuristic. (mặc định: 2)
        decay: Hệ số phân hủy pheromone. (mặc định: 0.05)
        local_search: Có thực hiện tìm kiếm cục bộ để cải thiện đường đi tốt nhất hay không. (mặc định: True)
        verbose: Có in thông tin tiến trình hay không. (mặc định: True)

    Returns:
        best_route: Đường đi ngắn nhất được tìm thấy bởi thuật toán ACO
        best_path_distance: Khoảng cách của đường đi ngắn nhất được tìm thấy bởi thuật toán ACO

    """
    count = 0
    best_route = []
    full_list = list(range(1, len(distance_matrix) + 1))
    distance = functions.sum_list(distance_matrix)
    h = attractiveness(distance_matrix)
    thau = functions.create_empty_matrix_ones(len(distance_matrix), len(distance_matrix))
    # Duyệt qua từng vòng lặp
    while (count <= iterations):
        # In ra thông tin tiến trình
        if (verbose == True and count > 0):
            print('Iteration = ', count, 'Distance = ', round(best_route[1], 2))
            # print(best_route)     
        city_list, path_distance, thau = ants_path(initial, distance_matrix, h, thau, alpha, beta, full_list, ants,
                                                   local_search)
        thau = functions.matrix_multiply(thau, 1 - decay)
        if (distance > path_distance):
            best_route = copy.deepcopy([city_list])
            best_route.append(path_distance)
            distance = best_route[1]
        count = count + 1
    route, distance = best_route
    return route, distance
