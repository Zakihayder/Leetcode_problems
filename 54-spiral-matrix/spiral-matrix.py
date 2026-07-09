class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []

        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # 1. Traverse Right (Top Row)
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1  # Move top boundary down

            # 2. Traverse Down (Right Column)
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1  # Move right boundary left

            # Check if a single row or column remains
            if top <= bottom:
                # 3. Traverse Left (Bottom Row)
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1  # Move bottom boundary up

            if left <= right:
                # 4. Traverse Up (Left Column)
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1  # Move left boundary right

        return result
        