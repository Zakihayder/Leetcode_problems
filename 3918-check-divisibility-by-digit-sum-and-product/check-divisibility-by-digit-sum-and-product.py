class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num = n
        total = 0
        product = 1
        while n > 0:
            remainder = n % 10
            total += remainder
            product *= remainder
            n = n // 10
        return (0 == num % (total+product))
        