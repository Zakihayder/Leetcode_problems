class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        start = 1
        digits = 1

        while start <= n:
            end = min(n, start * 10 - 1)

            commas = (digits - 1) // 3
            ans += (end - start + 1) * commas

            start *= 10
            digits += 1

        return ans