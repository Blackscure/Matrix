def get_maximum_minimum(matrix):
    result = []
    for i in range(len(matrix)):
        row_max = max(matrix[i])
        col_index = matrix[i].index(row_max)
        col_min = row_max
        for j in range(len(matrix)):
            if matrix[j][col_index] < col_min:
                col_min = matrix[j][col_index]
        if col_min == row_max:
            result.append(row_max)
    return result

matrix = [[5,16,20],[9,11,18],[15,16,17]]
result = get_maximum_minimum(matrix)
print(result) 
