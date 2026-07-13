class Solution(object):
    def trailingZeroes(self, n):
        
        count = 0
        power_of_5 = 5

        while power_of_5 <= n:
            count += n // power_of_5
            power_of_5 *= 5

        return count