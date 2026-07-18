class Solution(object):
    def findGCD(self, nums):
        def gcd(a,b):
            while b:
                a,b = b,a%b
            return a
        
        return gcd(max(nums),min(nums))
            