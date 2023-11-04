import math

# Function: Build Distance Matrix
def build_distance_matrix(data):
# Độ dài và độ rộng của ma trận
    num_rows = len(data)
    num_columns = len(data)

    # Tạo ma trận với giá trị ban đầu bằng 0 bằng cách sử dụng danh sách lồng nhau
    matrix = []
    for i in range(num_rows):
        row = []
        for j in range(num_columns):
            row.append(round(math.sqrt((data[i][0]-data[j][0])**2+(data[i][1]-data[j][1])**2),2))
        matrix.append(row)

    return matrix
