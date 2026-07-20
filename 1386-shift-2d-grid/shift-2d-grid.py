class Solution(object):
    def shiftGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total

        if k == 0:
            return grid

        def get(idx):
            i, j = divmod(idx, n)
            return grid[i][j]

        def set_val(idx, val):
            i, j = divmod(idx, n)
            grid[i][j] = val

        visited = 0
        start = 0

        while visited < total:
            cycle_start = start
            prev_val = get(start)
            curr_idx = start

            while True:
                next_idx = (curr_idx + k) % total
                next_val = get(next_idx)
                set_val(next_idx, prev_val)
                prev_val = next_val
                curr_idx = next_idx
                visited += 1
                if curr_idx == cycle_start:
                    break

            start += 1

        return grid