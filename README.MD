1. Initialize an empty list `result` to store the result.
2. For each row in the matrix:
    a. Find the maximum value in the row.
    b. Check if the maximum value is also the minimum value in its column.
        i. If yes, add it to the `result` list.
3. Return the `result` list.




The time complexity of the above solution is O(mn^2), where m is the number of rows and n is the number of columns in the matrix. This is because the outer loop runs m times and the inner loop runs n times for each iteration of the outer loop. In the inner loop, we are also checking each column of the matrix, which takes O(n) time. Hence, the total time complexity is O(mn^2).

The space complexity of the solution is O(m), as we are using a list to store the result. The list will have at most m elements, one for each row of the matrix. Hence, the space complexity is O(m).