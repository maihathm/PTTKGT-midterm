import math
import random

import ACO


def fitness_function():
    pass


def init_population(N=None, min_val=None, max_val=None, function=fitness_function, initial=1, distance_matrix=None):
    """
    Init population cho tập N bông hoa:
    :param N: là số lượng bông hoa
    :param min_val: là giá trị tối thiểu cu các biến đến từ list có thể có.
    :param max_val: là giá trị tối đa của các biến đến từ list có thể có.
    :param function: Hàm fitness
    :return: Population cho N bông hoa.
        ...
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
        print(f'alpha: {alpha}, beta: {beta}, decay {decay}')
        route, distance = function(initial, distance_matrix, alpha=float(alpha), beta=float(beta), decay=float(decay))
        position[i].append(distance)
    return position


# # TODO: Check init_population
# test_init_population = init_population(N=3, min_val=[0, 0, max_val=[5, 5], function=fitness_function)
# print("Test init population: ", test_init_population)


# Lévy flight
def levy_flight(beta=None):
    """
    # Tạo ra step-size parameter bằng lévy flight
    :param beta: Giá trị beta trong công thức
    :return: levy: Giá trị của Levy-flight
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
                       distance_matrix):
    """
    Thực hiện thụ phấn chéo

    :param  population: Là danh sách khởi tạo các bông hoa.
    :param best_global: Là đường đi tốt nhất trong lần chạy.
    :param flower: Vị trí bông hoa
    :param gamma: Giá trị của gamma trong công thức
    :param lamb: Giá trị Lamda trong công thức
    :param min_value: Các giá trị tối thiểu có thể nhận của Min_value
    :param max_value: Các gía trị tối đa có thể nhận của Max_value
    :param function: Hàm thích nghi.

    :return: Một đường đi thực hiện polination global.
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
    print(f'alpha: {alpha}, beta: {beta}, decay {decay}')
    route, x[-1] = function(initial, distance_matrix, alpha=float(alpha), beta=float(beta), decay=float(decay))
    return x


# pollination local
def pollination_local(population: [], best_global: [], flower, nb_flower1=None, nb_flower2=None, min_value=None,
                      max_value=None, function=None, initial=1, distance_matrix=None):
    """

    :param population: Danh sách khởi tạo các bông hoa
    :param best_global: Đường đi tốt nhất trong lần lặp trước
    :param flower: Bông hoa bắt đầu.
    :param nb_flower1: 
    :param nb_flower2: 
    :param min_value: Các giá trị thiểu có thể nhận
    :param max_value: Các gí trị tối đa có thể nhận
    :param function: Hàm thích nghi
    :return: Trả về đường đi thực hiện local polination
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
    print(type(alpha),type(beta),type(decay))
    route, x[-1] = function(initial, distance_matrix, alpha=float(alpha), beta=float(beta), decay=float(decay))
    return x


# Flower Pollination Algorithms
def flower_pollination_algorithms(flowers=3, min_values=None, max_values=None, iteration=50, gamma=0.5, lamb=1.4,
                                  p=0.8, initial=1, distance_matrix=None, function=None):
    """
    :param flowers: Bắt đầu từ bông hoa
    :param min_values: Các giá trị min có thể nhận
    :param max_values: Các giá trị max có thể nhận
    :param iteration: Số vòng lặp
    :param gamma: Giá trị của biến Gamma
    :param lamb: Giá trị của biến Lambda
    :param p: Xác suất chuyển đổi giữa Local Pollination vs Global Pollination
    :param function: Hàm thích nghi
    :return: Đường đi tốt nhất sử dụng thuật toán FPA.
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
