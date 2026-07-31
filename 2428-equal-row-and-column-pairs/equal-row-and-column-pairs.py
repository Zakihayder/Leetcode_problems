class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        transpose = [list(row) for row in zip(*grid)]
        count = 0
        for i in grid:
            for j in transpose:
                if i == j:
                    count += 1
        return count

        