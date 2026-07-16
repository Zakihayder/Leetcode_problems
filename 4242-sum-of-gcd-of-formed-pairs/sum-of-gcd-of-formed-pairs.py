class Solution(object):
    def gcdSum(self, nums):
        def gcd(a, b):
            # Euclidean algorithm — O(log(min(a,b))) instead of O(min(a,b))
            while b:
                a, b = b, a % b
            return a

        if not nums:
            return 0

        maximum = nums[0]
        GCD = []
        GCD.append(gcd(nums[0], maximum))  # gcd(x,x) = x, equivalent to your original line

        for i in range(1, len(nums)):
            if nums[i] > maximum:
                maximum = nums[i]
            GCD.append(gcd(nums[i], maximum))

        GCD.sort()
        total = 0
        for i in range(len(GCD) // 2):
            total += gcd(GCD[i], GCD[len(GCD) - 1 - i])

        return total