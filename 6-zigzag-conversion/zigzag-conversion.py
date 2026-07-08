class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows

        currRow = 0
        direction = 1   # 1 = down, -1 = up

        for ch in s:
            rows[currRow] += ch

            if currRow == 0:
                direction = 1
            elif currRow == numRows - 1:
                direction = -1

            currRow += direction

        return "".join(rows)