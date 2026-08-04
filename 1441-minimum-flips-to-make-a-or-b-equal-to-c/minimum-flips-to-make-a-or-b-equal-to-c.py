class Solution(object):
    def minFlips(self, a, b, c):
        ans = 0

        while a or b or c:
            abit = a & 1
            bbit = b & 1
            cbit = c & 1

            if cbit:
                if not (abit or bbit):
                    ans += 1
            else:
                ans += abit + bbit

            a >>= 1
            b >>= 1
            c >>= 1

        return ans