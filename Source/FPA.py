"""
Mã nguồn của thuật toán tối ưu hóa sử dụng giải thuật Flower Pollination Algorithm (FPA)
File này là một phần của việc triển khai giải thuật FPA để giải quyết bài toán tối ưu hóa cụ thể.
Liên quan đến việc tối ưu hóa các tham số alpha, beta, decay của ACO.
"""
import math
import random
import functions


def fitness_function():
    """
    Chưa được triển khai (đang giữ lại với lời gọi "pass"). Đây sẽ là hàm mục tiêu cần tối ưu hóa.
    """
    pass


def init_population(N:int=None, min_val:list[float]=None, max_val:list[float]=None, function=None, initial:int=1, distance_matrix:list[list[float]]=None)->list[list[int],float]:
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
    # Kiểm tra và gán giá trị mặc định cho số lượng cá thể, giá trị tối đa, và giá trị tối thiểu của mỗi tham số
    if N is None:
        N = 3
    if max_val is None:
        max_val = [5, 5, 5]
    if min_val is None:
        min_val = [0.001, 0.001, 0.001]

    # Khởi tạo danh sách 'position' để lưu trữ thông tin về các cá thể trong quần thể
    position = []

    # Duyệt qua mỗi cá thể trong quần thể
    for i in range(0, N):
        # Khởi tạo danh sách 'temp' để lưu trữ giá trị ngẫu nhiên của các tham số cho mỗi cá thể
        temp = []
        # Duyệt qua từng tham số và tạo giá trị ngẫu nhiên trong khoảng từ tối thiểu đến tối đa
        for j in range(0, len(min_val)):
            random_val = random.uniform(min_val[j], max_val[j])
            temp.append(random_val)
        # Thêm danh sách 'temp' vào danh sách 'position'
        position.append(temp)

    # Đánh giá mỗi cá thể và tính toán giá trị khoảng cách
    for i in range(0, N):
        # Lấy giá trị tham số từ cá thể thứ i
        val = position[i][0: len(position[i])]
        alpha, beta, decay = val
        # Gọi hàm 'function' để tính toán giá trị 'route' và 'distance' dựa trên tham số của cá thể
        route, distance = function(
            initial=initial,
            distance_matrix=distance_matrix,
            alpha=float(alpha),
            beta=float(beta),
            decay=float(decay),
            local_search=False
        )
        # Thêm giá trị khoảng cách đã tính toán vào danh sách của cá thể tương ứng trong 'position'
        position[i].append(distance)
    return position


# Lévy flight
def levy_flight(beta:float=None)->float:
    """
    Tạo ra một bước nhảy Lévy với tham số beta

    Args:
        beta: Tham số beta của phân bố Lévy-Stable (nếu không được cung cấp, giá trị mặc định là 1.5)

    Returns:
        Bước nhảy Lévy
    """
    # Kiểm tra và gán giá trị mặc định cho tham số beta
    if beta is None:
        beta = 1.5

    # Tạo các giá trị ngẫu nhiên
    r1 = random.uniform(0, 1)
    r2 = random.uniform(0, 1)

    # Tính toán các thành phần của phân phối Lévy-Stable
    sig_num = math.gamma((1 + beta)) * math.sin((math.pi * beta) / 2.0)
    sig_den = math.gamma((1 + beta) / 2) * beta * 2 ** ((beta - 1) / 2)

    # Tính toán giá trị sigma
    sigma = (sig_num / sig_den) ** (1 / beta)

    # Tính toán và trả về bước nhảy Lévy
    levy = (0.01 * r1 * sigma) / (abs(r2) ** (1 / beta))
    return levy


# pollination global
def pollination_global(population: list[list[int],float], best_global: list[list[int],float], flower:int, gamma:float, lamb:float,
                       min_value:list[float], max_value:list[float], function, initial:int,
                       distance_matrix:list[list[float]], distance:float=None)->list[list[int],float]:
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
        distance: Giá trị đạt được tốt nhất đã biết

    Returns:
        Cá thể được cập nhật sau khi thực hiện phép thụ phấn toàn cầu
    """
    # Tạo một bản sao của cá thể tốt nhất toàn cầu để cập nhật
    x = best_global.copy()

    # Duyệt qua từng tham số của cá thể và cập nhật giá trị dựa trên thuật toán FPA
    for j in range(0, len(min_value)):
        value = population[flower][j] + gamma * levy_flight(lamb) * (population[flower][j] - best_global[j])
        # Kiểm tra giá trị mới và đảm bảo nằm trong khoảng tối thiểu và tối đa
        if value < min_value[j]:
            value = min_value[j]
        if value > max_value[j]:
            value = max_value[j]

        # Cập nhật giá trị trong cá thể được sao chép từ cá thể tốt nhất toàn cầu
        x[j] = value

    # Lấy giá trị tham số từ cá thể được cập nhật
    alpha, beta, decay = x[0:len(min_value)]

    # Gọi hàm mục tiêu để tính toán giá trị tuyến đường và khoảng cách
    route, x[-1] = function(
        initial=initial,
        distance_matrix=distance_matrix,
        alpha=float(alpha),
        beta=float(beta),
        decay=float(decay),
        local_search=False,
        current_best_distance=distance)

    return x


def pollination_local(population: list[list[int],float], best_global: list[list[int],float], flower:int, nb_flower1:float=None, nb_flower2:float=None, min_value:list[float]=None,
                      max_value:list[float]=None, function=None, initial:int=1, distance_matrix:list[list[float]]=None, distance:float=None)->list[list[int],float]:
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
        distance: Giá trị đạt được tốt nhất đã biết
    Returns:
        Cá thể được cập nhật sau khi thực hiện phép thụ phấn địa phương
    """
    if nb_flower1 is None:
        nb_flower1 = 0
    if nb_flower2 is None:
        nb_flower2 = 1
    x = best_global.copy()
    for j in range(0, len(min_value)):
        # r là 1 số ngẫu nhiên từ 0 đến 1
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
    route, x[-1] = function(initial, distance_matrix, alpha=float(alpha), beta=float(beta), decay=float(decay),
                            local_search=False, current_best_distance=distance)
    # Trả về bông hoa x sau khi cập nhật local pollination.
    return x


# Flower Pollination Algorithms
def flower_pollination_algorithms(flowers:int=3, position:list[list[int],float]=None, min_values:list[float]=None, max_values:list[float]=None,
                                  iteration:int=50, gamma:float=0.5,lamb:float=1.4,
                                  p:float=0.8, initial:int=1, distance_matrix:list[list[float]]=None, function=None, distance:float=None)->list[list[int],float]:
    """
    Tối ưu hóa dựa trên quần thể FPA

    Args:
        flowers: Số lượng cá thể trong quần thể (nếu không được cung cấp, giá trị mặc định là 3)
        position: vị trí của phấn hoa
        min_values: Danh sách các giá trị tối thiểu cho mỗi tham số cá thể (nếu không được cung cấp, giá trị mặc định là `[0, 0, 0]`)
        max_values: Danh sách các giá trị tối đa cho mỗi tham số cá thể (nếu không được cung cấp, giá trị mặc định là `[5, 5, 5]`)
        iteration: Số lượng lặp của thuật toán (nếu không được cung cấp, giá trị mặc định là 50)
        gamma: Tham số gamma của phép thụ phấn toàn cầu (nếu không được cung cấp, giá trị mặc định là 0.5)
        lamb: Tham số lambda của phép bay Lévy (nếu không được cung cấp, giá trị mặc định là 1.4)
        p: Xác suất chọn phép thụ phấn toàn cầu (nếu không được cung cấp, giá trị mặc định là 0.8)
        initial: Giá trị ban đầu của tuyến đường (nếu không được cung cấp, giá trị mặc định là 1)
        distance_matrix: Ma trận khoảng cách giữa các điểm trong tuyến đường (nếu không được cung cấp, giá trị mặc định là `None`)
        function: Hàm mục tiêu được sử dụng để đánh giá mỗi cá thể trong quần thể
        distance: Giá trị đạt được tốt nhất đã biết
    Returns:
        Cá thể tốt nhất toàn cầu
    """
    # Thiết lập giá trị mặc định nếu không được cung cấp
    if max_values is None:
        max_values = [5, 5, 5]
    if min_values is None:
        min_values = [0, 0, 0]
    count = 0

    # Khởi tạo quần thể nếu không được cung cấp
    if position is None:
        position = init_population(N=flowers, min_val=min_values, function=function, max_val=max_values, initial=initial
                                   , distance_matrix=distance_matrix)

    # Tìm cá thể tốt nhất toàn cầu trong quần thể ban đầu
    best_global = functions.find_best_global(position)
    x = best_global.copy()

    # Bắt đầu vòng lặp chính của thuật toán
    for loop in range(iteration + 1):
        for i in range(0, len(position)):
            nb_flower_1 = random.randint(0, len(position) - 1)
            nb_flower_2 = random.randint(0, len(position) - 1)
            # Đảm bảo chọn hai cá thể khác nhau
            while nb_flower_1 == nb_flower_2:
                nb_flower_2 = random.randint(0, len(position) - 1)
            r = random.uniform(0, 1)
            # Thực hiện phép thụ phấn toàn cầu hoặc địa phương tùy thuộc vào giá trị ngẫu nhiên r
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
                    distance_matrix=distance_matrix,
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
                    distance_matrix=distance_matrix,
                )

            # So sánh khoảng cách của cá thể đã cập nhật với cá thể hiện tại
            if x[-1] <= position[i][-1]:
                for j in range(0, len(position[0])):
                    position[i][j] = x[j]

            # Tìm cá thể tốt nhất trong quần thể sau mỗi cập nhật
            val = functions.find_best_global(position)
            if best_global[-1] > val[-1]:
                best_global = val
    return best_global

