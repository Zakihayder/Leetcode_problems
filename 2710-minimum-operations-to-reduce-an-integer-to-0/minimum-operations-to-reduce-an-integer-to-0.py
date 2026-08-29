class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0

        while n:
            if n % 2 == 0:
                n //= 2
                continue

            if n == 1:
                ans += 1
                break

            if n % 4 == 1:
                n -= 1
            else:
                n += 1

            ans += 1

        return ans