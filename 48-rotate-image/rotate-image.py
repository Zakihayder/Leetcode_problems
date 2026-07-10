class Solution(object):
    def rotate(self, matrix):
        # Correctly initialize a 2D matrix clone
        matrix1 = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
        n = len(matrix)
        
        rows = -1
        cols = -1
        for i in matrix:
            rows += 1
            for j in i:
                cols += 1
                # Adjusted formula to grab elements from bottom to top of columns
                matrix1[rows][cols] = matrix[n - cols - 1][rows]
            cols = -1
            
        # In-place copy to satisfy LeetCode's modification requirement
        for r in range(n):
            for c in range(n):
                matrix[r][c] = matrix1[r][c]
