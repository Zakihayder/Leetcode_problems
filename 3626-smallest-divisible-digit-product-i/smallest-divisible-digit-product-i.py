class Solution(object):
    def smallestNumber(self, n, t):
        while True:
            product = 1
            x = n

            while x:
                product *= x % 10
                x //= 10

            if product % t == 0:
                return n

            n += 1