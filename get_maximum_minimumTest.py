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

# Test 1
matrix = [[100,60,20, 50],[70,80,10,90],[10,50,44,30]]
result = get_maximum_minimum(matrix)
assert result == [50], f"Expected [50] but got {result}"

# Test 2
matrix = [[5,16,20],[9,11,18],[15,16,17]]
result = get_maximum_minimum(matrix)
assert result == [17], f"Expected [17] but got {result}"

print("All tests passed!")