import math
import random


def fitness_function():
    pass


def init_population(N=None, min_val=None, max_val=None, function=None, initial=1, distance_matrix=None):
    """
    Khởi tạo quần thể cá thể ban đầu cho thuật toán tối ưu hóa dựa trên quần thể.

    Args:
        N: Số lượng cá thể trong quần thể (nếu không được cung cấp, giá trị mặc định là 3)
        min_val: Danh sách các giá trị tối thiểu cho mỗi tham số cá thể (nếu không được cung cấp, giá trị mặc định là `[0.001, 0.001, 0.001]`)
        max_val: Danh sách các giá trị tối đa cho mỗi tham số cá thể (nếu không được cung cấp, giá trị mặc định là `[5, 5, 5]`)
        function: Hàm mục tiêu được sử dụng để đánh giá mỗi cá thể trong quần thể (nếu không được cung cấp, giá trị mặc định là hàm `target_function`)
        initial: Giá trị ban đầu của tuyến đường (nếu không được cung cấp, giá trị mặc định là 1)
        distance_matrix: Ma trận khoảng cách giữa các điểm trong tuyến đường (nếu không được cung cấp, giá trị mặc định là `None`)

    Returns:
        Danh sách các cá thể
    """
    if N is None:
        N = 3
    if max_val is None:
        max_val = [5, 5, 5]
    if min_val is None:
        min_val = [0.001, 0.001, 0.001]

    position = []
    for i in range(0, N):
        temp = []
        for j in range(0, len(min_val)):
            random_val = random.uniform(min_val[j], max_val[j])
            temp.append(random_val)
        position.append(temp)
    for i in range(0, N):
        val = position[i][0: len(position[i])]
        alpha, beta, decay = val
        # print(type(alpha),type(beta),type(decay))
        # print(f'alpha: {alpha}, beta: {beta}, decay {decay}')
        route, distance = function(
            initial=initial,
            distance_matrix=distance_matrix,
            alpha=float(alpha),
            beta=float(beta),
            decay=float(decay),
            local_search=False
        )
        position[i].append(distance)
    return position


# # TODO: Check init_population
# test_init_population = init_population(N=3, min_val=[0, 0, max_val=[5, 5], function=fitness_function)
# print("Test init population: ", test_init_population)


# Lévy flight
def levy_flight(beta=None):
    """
    Tạo ra một bước nhảy Lévy với tham số beta

    Args:
        beta: Tham số beta của phân bố Lévy-Stable (nếu không được cung cấp, giá trị mặc định là 1.5)

    Returns:
        Bước nhảy Lévy
    """
    if beta is None:
        beta = 1.5
    r1 = random.uniform(0, 1)
    r2 = random.uniform(0, 1)
    sig_num = math.gamma((1 + beta)) * math.sin((math.pi * beta) / 2.0)
    sig_den = math.gamma((1 + beta) / 2) * beta * 2 ** ((beta - 1) / 2)
    sigma = (sig_num / sig_den) ** (1 / beta)
    levy = (0.01 * r1 * sigma) / (abs(r2) ** (1 / beta))
    return levy


# # test Lévy flight
# levy_ = levy_flight(beta=1.5)
# print("Levy flight: ", levy_)  # 0.005528715490671566 -> Oke


# pollination global
def pollination_global(population: [], best_global: [], flower, gamma, lamb, min_value, max_value, function, initial,
                       distance_matrix, distance=None):
    """
    Thực hiện phép thụ phấn toàn cầu trong thuật toán FPA

    Args:
        population: Danh sách các cá thể trong quần thể
        best_global: Cá thể tốt nhất toàn cầu
        flower: Cá thể đang được cập nhật
        gamma: Tham số gamma của phép thụ phấn
        lamb: Tham số lambda của phép bay Lévy
        min_value: Danh sách các giá trị tối thiểu cho mỗi tham số cá thể
        max_value: Danh sách các giá trị tối đa cho mỗi tham số cá thể
        function: Hàm mục tiêu được sử dụng để đánh giá mỗi cá thể trong quần thể
        initial: Giá trị ban đầu của tuyến đường
        distance_matrix: Ma trận khoảng cách giữa các điểm trong tuyến đường

    Returns:
        Cá thể được cập nhật sau khi thực hiện phép thụ phấn toàn cầu
    """

    x = best_global.copy()
    for j in range(0, len(min_value)):
        value = population[flower][j] + gamma * levy_flight(lamb) * (population[flower][j] - best_global[j])
        if value < min_value[j]:
            value = min_value[j]
        if value > max_value[j]:
            value = max_value[j]
        x[j] = value
    alpha, beta, decay = x[0:len(min_value)]
    # print(type(alpha),type(beta),type(decay))
    # print(f'alpha: {alpha}, beta: {beta}, decay {decay}')
    route, x[-1] = function(
        initial=initial,
        distance_matrix=distance_matrix,
        alpha=float(alpha),
        beta=float(beta),
        decay=float(decay),
        local_search=False,
        current_best_distance=distance)
    return x


# pollination local
def pollination_local(population: [], best_global: [], flower, nb_flower1=None, nb_flower2=None, min_value=None,
                      max_value=None, function=None, initial=1, distance_matrix=None, distance=None):
    """
    Thực hiện phép thụ phấn địa phương trong thuật toán FPA

    Args:
        population: Danh sách các cá thể trong quần thể
        best_global: Cá thể tốt nhất toàn cầu
        flower: Cá thể đang được cập nhật
        nb_flower1: Chỉ số của cá thể thứ nhất được sử dụng trong phép thụ phấn (nếu không được cung cấp, giá trị mặc định là 0)
        nb_flower2: Chỉ số của cá thể thứ hai được sử dụng trong phép thụ phấn (nếu không được cung cấp, giá trị mặc định là 1)
        min_value: Danh sách các giá trị tối thiểu cho mỗi tham số cá thể
        max_value: Danh sách các giá trị tối đa cho mỗi tham số cá thể
        function: Hàm mục tiêu được sử dụng để đánh giá mỗi cá thể trong quần thể
        initial: Giá trị ban đầu của tuyến đường
        distance_matrix: Ma trận khoảng cách giữa các điểm trong tuyến đường

    Returns:
        Cá thể được cập nhật sau khi thực hiện phép thụ phấn địa phương
    """
    if nb_flower1 is None:
        nb_flower1 = 0
    if nb_flower2 is None:
        nb_flower2 = 1
    x = best_global.copy()
    for j in range(0, len(min_value)):
        r = random.uniform(0, 1)
        val = population[flower][j] + r * (population[nb_flower1][j] - population[nb_flower2][j])
        if val < min_value[j]:
            val = min_value[j]
        if val > max_value[j]:
            val = max_value[j]
        x[j] = val
    alpha, beta, decay = x[0:len(min_value)]
    # print(type(alpha),type(beta),type(decay))
    route, x[-1] = function(initial, distance_matrix, alpha=float(alpha), beta=float(beta), decay=float(decay),
                            local_search=False, current_best_distance=distance)
    return x


# Flower Pollination Algorithms
def flower_pollination_algorithms(flowers=3, position=None, min_values=None, max_values=None, iteration=50, gamma=0.5,
                                  lamb=1.4,
                                  p=0.8, initial=1, distance_matrix=None, function=None, distance=None):
    """
    Tối ưu hóa dựa trên quần thể FPA

    Args:
        flowers: Số lượng cá thể trong quần thể (nếu không được cung cấp, giá trị mặc định là 3)
        min_values: Danh sách các giá trị tối thiểu cho mỗi tham số cá thể (nếu không được cung cấp, giá trị mặc định là `[0, 0, 0]`)
        max_values: Danh sách các giá trị tối đa cho mỗi tham số cá thể (nếu không được cung cấp, giá trị mặc định là `[5, 5, 5]`)
        iteration: Số lượng lặp của thuật toán (nếu không được cung cấp, giá trị mặc định là 50)
        gamma: Tham số gamma của phép thụ phấn toàn cầu (nếu không được cung cấp, giá trị mặc định là 0.5)
        lamb: Tham số lambda của phép bay Lévy (nếu không được cung cấp, giá trị mặc định là 1.4)
        p: Xác suất chọn phép thụ phấn toàn cầu (nếu không được cung cấp, giá trị mặc định là 0.8)
        initial: Giá trị ban đầu của tuyến đường (nếu không được cung cấp, giá trị mặc định là 1)
        distance_matrix: Ma trận khoảng cách giữa các điểm trong tuyến đường (nếu không được cung cấp, giá trị mặc định là `None`)
        function: Hàm mục tiêu được sử dụng để đánh giá mỗi cá thể trong quần thể

    Returns:
        Cá thể tốt nhất toàn cầu
    """
    if max_values is None:
        max_values = [5, 5, 5]
    if min_values is None:
        min_values = [0, 0, 0]
    count = 0
    if position is None:
        # print("Khởi tạo bông hoa")
        position = init_population(N=flowers, min_val=min_values, function=function, max_val=max_values, initial=initial
                                   , distance_matrix=distance_matrix)
    # else:
    #     print("Đã khởi tạo bông hoa")
    best_global = sorted(position, key=lambda x: x[-1])[0]
    x = best_global.copy()
    for loop in range(iteration + 1):
        print(f"Vòng lặp thứ {loop}, f(x) = {best_global}")
        for i in range(0, len(position)):
            nb_flower_1 = random.randint(0, len(position) - 1)
            nb_flower_2 = random.randint(0, len(position) - 1)
            while nb_flower_1 == nb_flower_2:
                nb_flower_2 = random.randint(0, len(position) - 1)
            r = random.uniform(0, 1)

            if r < p:
                # print("Global Pollination")
                x = pollination_global(
                    population=position,
                    best_global=best_global,
                    flower=i,
                    gamma=gamma,
                    lamb=lamb,
                    min_value=min_values,
                    max_value=max_values,
                    function=function,
                    initial=initial,
                    distance_matrix=distance_matrix,


                    # distance=distance  # Khoảng cách tốt nhất hiện tại
                )
            else:
                # print("Local Pollination")
                x = pollination_local(
                    population=position,
                    flower=i,
                    function=function,
                    max_value=max_values,
                    min_value=min_values,
                    nb_flower2=nb_flower_2,
                    nb_flower1=nb_flower_1,
                    best_global=best_global,
                    initial=initial,
                    distance_matrix=distance_matrix,

                    # distance=distance  # Khoảng cách tốt nhất hiện tại
                )
            if x[-1] <= position[i][-1]:
                for j in range(0, len(position[0])):
                    position[i][j] = x[j]
            val = sorted(position, key=lambda x: x[-1])[0]
            if best_global[-1] > val[-1]:
                # print("Updated best global")
                best_global = val
    return best_global
