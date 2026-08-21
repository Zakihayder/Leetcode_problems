class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            total = 0

            for mask in range(1, 1 << n):
                common = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        common = lcm(common, coins[i])

                        if common > x:
                            break

                if common > x:
                    continue

                if bits & 1:
                    total += x // common
                else:
                    total -= x // common

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = left + (right - left) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left