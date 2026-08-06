class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        ans = [[1], [1, 1]]

        for i in range(3, numRows + 1):
            row = []

            for j in range(i):
                if j == 0 or j == i - 1:
                    row.append(1)
                else:
                    row.append(ans[-1][j - 1] + ans[-1][j])

            ans.append(row)

        return ans