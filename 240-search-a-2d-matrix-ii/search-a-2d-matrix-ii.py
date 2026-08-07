class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(len(matrix)):
            if matrix[i][0] > target:
                return False
            for j in range(len(matrix[0])):
                if matrix[i][j] > target:
                    break
                if  matrix[i][j] == target:
                    return True
        return False
            
