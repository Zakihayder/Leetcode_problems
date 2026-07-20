class Solution(object):
    def shiftGrid(self, grid, k):

        m, n = len(grid), len(grid[0])
        total = m * n

        k %= total

        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                flat_index = i * n + j
                new_flat_index = (flat_index + k) % total
                new_i, new_j = divmod(new_flat_index, n)
                result[new_i][new_j] = grid[i][j]

        return result