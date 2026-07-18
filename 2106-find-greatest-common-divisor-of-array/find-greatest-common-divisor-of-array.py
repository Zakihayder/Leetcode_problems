class Solution(object):
    def findGCD(self, nums):
        a = max(nums)
        b = min(nums)

        while b:
            a,b = b,a%b

        return a
        