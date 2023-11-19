# Function: Tour Distance
import copy


def distance_calc(distance_matrix, city_tour):
    """Tính tổng khoảng cách của một tour du lịch.

  Args:
    distance_matrix: Ma trận khoảng cách giữa các thành phố. [ ]
    city_tour: Một tour du lịch, được biểu diễn bằng một danh sách các thành phố
      theo thứ tự tham quan.

  Returns:
    Tổng khoảng cách của tour du lịch.
  """
    distance = 0
    for k in range(0, len(city_tour[0]) - 1):
        m = k + 1
        city_k = city_tour[0][k]
        city_m = city_tour[0][m]
        distance = distance + distance_matrix[city_k - 1][city_m - 1]
    return distance


# Function: 2_opt
def local_search_2_opt(distance_matrix, city_tour, recursive_seeding=-1):
    """Tìm kiếm cục bộ 2-opt để cải thiện tour du lịch.

  Args:
    distance_matrix: Ma trận khoảng cách giữa các thành phố.
    city_tour: Một tour du lịch, được biểu diễn bằng một danh sách các thành phố
      theo thứ tự tham quan.
    recursive_seeding: Số lần lặp của thuật toán tìm kiếm cục bộ 2-opt.
      Nếu `      < 0`, thuật toán sẽ chạy cho đến khi không thể cải thiện
      tour du lịch được nữa.

  Returns:
    Một tour du lịch được cải thiện, tổng khoảng cách tour du lịch được cải thiện. Được biểu diễn bằng một danh sách các thành phố
      theo thứ tự tham quan.
  """
    if (recursive_seeding < 0):
        count = -2
    else:
        count = 0
    city_list = copy.deepcopy(city_tour)
    distance = city_list[1] * 2
    while (count < recursive_seeding):
        best_route = copy.deepcopy(city_list)
        seed = copy.deepcopy(city_list)
        # Duyệt qua tất cả các cặp đoạn đường trong tour du lịch
        for i in range(1, len(city_list[0]) - 2):
            for j in range(i + 1, len(city_list[0]) - 1):
                # Hoán đổi hai đoạn đường đó và tính lại tổng khoảng cách của tour du lịch
                best_route[0][i:j + 1] = list(reversed(best_route[0][i:j + 1]))
                best_route[0][-1] = best_route[0][0]
                best_route[1] = distance_calc(distance_matrix, best_route)
                # Nếu tổng khoảng cách của tour du lịch sau khi hoán đổi nhỏ hơn tổng khoảng cách tour du lịch ban đầu
                if (city_list[1] > best_route[1]):
                    # Thực hiện hoán đổi
                    city_list = copy.deepcopy(best_route)
                best_route = copy.deepcopy(seed)
        count = count + 1
        # Tiếp tục xét số lần lặp
        if (distance > city_list[1] and recursive_seeding < 0):
            distance = city_list[1]
            count = -2
            recursive_seeding = -1
        elif (city_list[1] >= distance and recursive_seeding < 0):
            count = -1
            recursive_seeding = -2
    return city_list[0], city_list[1]
