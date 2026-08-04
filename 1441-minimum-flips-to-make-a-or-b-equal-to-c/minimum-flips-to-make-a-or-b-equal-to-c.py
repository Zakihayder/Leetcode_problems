class Solution(object):
    def minFlips(self, a, b, c):
        ans = 0

        while a or b or c:
            if c & 1:
                ans += ((a | b) & 1) == 0
            else:
                ans += (a & 1) + (b & 1)

            a >>= 1
            b >>= 1
            c >>= 1

        return ans