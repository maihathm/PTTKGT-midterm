import random
import math


def fitness_function():
    pass


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
        temp.clear()
        for j in range(0, len(min_val)):
            # print("j: ", j)
            temp.append(
                random.uniform(min_val[j], max_val[j])
            )

            temp.append(0.0)
        position.append(temp)
    # print("Position: ", position)
    return position


# test:
test_init_population = init_population(N=5)
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