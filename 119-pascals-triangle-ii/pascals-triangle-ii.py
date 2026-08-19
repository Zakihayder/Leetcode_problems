class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]

        ans = [[1], [1, 1]]

        for i in range(2, rowIndex + 2):
            row = []

            for j in range(i):
                if j == 0 or j == i - 1:
                    row.append(1)
                else:
                    row.append(ans[-1][j - 1] + ans[-1][j])

            ans.append(row)

        return ans[-1]