import random
import math


def fitness_function():
    pass


def six_hump_camel_back(variables_value=None):
    if variables_value is None:
        variables_value = [0, 0]
    return 4 * variables_value[0] ** 2 - 2.1 * variables_value[0] ** 4 + (1 / 3) * variables_value[0] ** 6 + \
        variables_value[0] * variables_value[1] - 4 * variables_value[1] ** 2 + 4 * variables_value[1] ** 4


def init_population(N=None, min_val=None, max_val=None, function=fitness_function()):
    """
    Init population cho tập N bông hoa:
    :param N: là số lượng bông hoa
    :param min_val: là giá trị tối thiểu cu các biến đến từ list có thể có.
    :param max_val: là giá trị tối đa của các biến đến từ list có thể có.
    :param function:
    :return:
        ...
    """
    if N is None:
        N = 3
    if max_val is None:
        max_val = [5, 5]
    if min_val is None:
        min_val = [-5, -5]

    position = []
    temp = []
    for i in range(0, N):
        temp = []
        for j in range(0, len(min_val)):
            # print("j: ", j)
            random_val = random.uniform(min_val[j], max_val[j])
            # print("random_val: ", random_val)
            temp.append(
                random_val
            )
        # print("Temp: ", temp)
        position.append(temp)
    # print("Position: ", position)
    for i in range(0, N):
        val = position[i][0: len(position[i])]
        # print("val: ",val)
        temp = function(
            val
        )
        # print("Temp: ",temp)
        position[i].append(
            temp
        )
    return position


# test:
test_init_population = init_population(N=3, function=six_hump_camel_back)
print(test_init_population)


# Lévy flight
def levy_flight(beta=None):
    """
    # Tạo ra step-size parameter bằng lévy flight
    :param beta:
    :return: levy
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


# test Lévy flight
levy_ = levy_flight(beta=1.5)
print(levy_)


# pollination global
def pollination_global(population: [], best_global: [], flower, gamma, lamb, min_value, max_value, function):
    """
    Thực hiện thụ phấn chéo

    :param  population:
    :param best_global:
    :param flower:
    :param gamma:
    :param lamb:
    :param min_value:
    :param max_value:
    :param function:

    :return:
    """

    x = best_global.copy()
    # TODO: continues
    for j in range(0, len(min_value)):
        value = population[flower][j] + gamma * levy_flight(lamb) * (population[flower][j] - best_global[j])
        if value < min_value[j]:
            value = min_value[j]
        if value > max_value[j]:
            value = max_value[j]

        x[j] = value
    # print("x prev", x)
    x[-1] = function(x[0:len(min_value)])
    # print("x aft", x)
    return x


# test pollination_global
pg = pollination_global(
    population=test_init_population,
    function=six_hump_camel_back,
    best_global=[1, 4, 5],
    flower=0,
    max_value=[5, 5],
    min_value=[-5, -5],
    gamma=0.5,
    lamb=1.4
)
print("Global pollination:", pg)


# pollination local
def pollination_local(population: [], best_global: [], flower, nb_flower1=None, nb_flower2=None, min_value=None,
                      max_value=None, function=fitness_function()):
    # print(f"nb_flower1 {nb_flower1}, nb_flower2 {nb_flower2}")
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
    x[-1] = function(x[0:len(min_value)])
    return x


pl = pollination_local(
    population=test_init_population,
    best_global=[1, 4, 5],
    flower=0,
    nb_flower1=0,
    nb_flower2=1,
    function=six_hump_camel_back,
    min_value=[-5, -5],
    max_value=[5, 5],
)
print("Pollination locally:", pl)


# Flower Pollination Algorithms
def flower_pollination_algorithms(flowers=3, min_values=None, max_values=None, iteration=50, gamma=0.5, lamb=1.4,
                                  p=0.8, function=six_hump_camel_back):
    """

    :param flowers:
    :param min_values:
    :param max_values:
    :param iteration:
    :param gamma:
    :param lamb:
    :param p:
    :param function:
    :return:
    """

    if max_values is None:
        max_values = [5, 5]
    if min_values is None:
        min_values = [-5, -5]
    count = 0
    position = init_population(N=flowers, min_val=min_values, function=function, max_val=max_values)
    last = []
    for index, att in enumerate(position):
        # print("index:", index)
        # print("att:", att)
        last.append([att[-1], index])
    last.sort()
    # print("Last:", last)
    arr_last = []
    for i in last:
        arr_last.append(i[-1])
    # print("arr_last:", arr_last)
    position_sorted = []
    for i in arr_last:
        position_sorted.append(
            position[i]
        )
    # print("position_sorted:", position_sorted)

    best_global = position_sorted[0]
    # print("best_global:", best_global)
    x = best_global.copy()
    for loop in range(iteration + 1):
        print(f"Vòng lặp thứ {loop}, f(x) = {best_global}")
        # print("x: ", x)
        for i in range(0, len(position)):
            nb_flower_1 = random.randint(0, len(position) - 1)
            nb_flower_2 = random.randint(0, len(position) - 1)
            while nb_flower_1 == nb_flower_2:
                nb_flower_2 = random.randint(0, len(position) - 1)
            r = random.uniform(0, 1)

            if r < p:
                # print("Global")
                x = pollination_global(
                    population=position,
                    best_global=best_global,
                    flower=i,
                    gamma=gamma,
                    lamb=lamb,
                    min_value=min_values,
                    max_value=max_values,
                    function=function
                )
            else:
                # print("Local")
                x = pollination_local(
                    population=position,
                    flower=i,
                    function=function,
                    max_value=max_values,
                    min_value=min_values,
                    nb_flower2=nb_flower_2,
                    nb_flower1=nb_flower_1,
                    best_global=best_global
                )
            # print("x: ", x)
            if x[-1] <= position[i][-1]:
                # print("Changed")
                for j in range(0, len(position[0])):
                    position[i][j] = x[j]
            val = sorted(position, key=lambda x: x[-1])[0]
            # print("Val: ", val)
            if best_global[-1] > val[-1]:
                best_global = val

    return best_global


fpa = flower_pollination_algorithms(flowers=5, min_values=[-5, -5], max_values=[5, 5], iteration=50, gamma=0.1,
                                    lamb=1.5, p=0.8, function=six_hump_camel_back)