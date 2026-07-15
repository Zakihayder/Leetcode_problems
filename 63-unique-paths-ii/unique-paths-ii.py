class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        # if the starting cell itself is an obstacle, no paths exist at all
        if obstacleGrid[0][0] == 1:
            return 0

        obstacleGrid[0][0] = 1  # reuse the grid to store path counts; start = 1 way

        # fill in the first row: can only come from the left, blocked by any obstacle
        for j in range(1, cols):
            obstacleGrid[0][j] = 0 if obstacleGrid[0][j] == 1 else obstacleGrid[0][j - 1]

        # fill in the first column: can only come from above, blocked by any obstacle
        for i in range(1, rows):
            obstacleGrid[i][0] = 0 if obstacleGrid[i][0] == 1 else obstacleGrid[i - 1][0]

        # fill in the rest of the grid
        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0  # obstacle — no paths reach here
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]

        return obstacleGrid[rows - 1][cols - 1]