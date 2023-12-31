import math
import random

import ACO


def target_function():
    pass


def init_population(N:int = None, min_val:list = None, max_val:list = None, function=target_function, initial:int =1, distance_matrix:list = None)->list:
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
        print(f'alpha: {alpha}, beta: {beta}, decay {decay}')
        route, distance = function(initial, distance_matrix, alpha=float(alpha), beta=float(beta), decay=float(decay))
        position[i].append(distance)
    return position

# Lévy flight
def levy_flight(beta: float=None)->float:
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

# pollination global
def pollination_global(population: [], best_global: [], flower:int, gamma:float, lamb:float, min_value:list, max_value:list, function, initial:int,
                       distance_matrix:list)->list:
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
    print(f'alpha: {alpha}, beta: {beta}, decay {decay}')
    route, x[-1] = function(initial, distance_matrix, alpha=float(alpha), beta=float(beta), decay=float(decay))
    return x


# pollination local
def pollination_local(population: [], best_global: [], flower:int , nb_flower1:float=None, nb_flower2:float=None, min_value:list=None,
                      max_value:list=None, function=None, initial:int=1, distance_matrix:list=None)->list:
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
    # r là 1 số ngẫu nhiên từ 0 đến 1
    for j in range(0, len(min_value)):
        r = random.uniform(0, 1)
        # val bằng với bông hoa hiện tại + r (hiệu 2 vị trí 2 bông hoa vị trí j và k (khác nhau))
        val = population[flower][j] + r * (population[nb_flower1][j] - population[nb_flower2][j])
        if val < min_value[j]:
            val = min_value[j]
        if val > max_value[j]:
            val = max_value[j]
        # Cập nhật x_j thành val
        x[j] = val
    # Gán lại giá trị cho val.
    alpha, beta, decay = x[0:len(min_value)]
    print(f'alpha: {alpha}, beta: {beta}, decay {decay}')
    route, x[-1] = function(initial, distance_matrix, alpha=float(alpha), beta=float(beta), decay=float(decay))
    # Trả về bông hoa x sau khi cập nhật local pollination.
    return x


# Flower Pollination Algorithms
def flower_pollination_algorithms(flowers:int=3, min_values:list=None, max_values:list=None, iteration:int=50, gamma:float=0.5, lamb:float=1.4,
                                  p:float=0.8, initial:float=1, distance_matrix:list=None, function=None)->list:
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
    position = init_population(N=flowers, min_val=min_values, function=function, max_val=max_values, initial=initial
                               , distance_matrix=distance_matrix)
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
                    distance_matrix=distance_matrix
                )
            else:
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
                    distance_matrix=distance_matrix
                )
            if x[-1] <= position[i][-1]:
                for j in range(0, len(position[0])):
                    position[i][j] = x[j]
            val = sorted(position, key=lambda x: x[-1])[0]
            if best_global[-1] > val[-1]:
                best_global = val
    return best_global
