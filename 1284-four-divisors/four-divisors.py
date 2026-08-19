class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0

        for n in nums:
            count = 2
            total = 1 + n

            i = 2
            while i <= n // i:
                if n % i == 0:
                    count += 1
                    total += i

                    if i != n // i:
                        count += 1
                        total += n // i

                    if count > 4:
                        break

                i += 1

            if count == 4:
                ans += total

        return ans