class Solution(object):
    def singleNumber(self, nums):
        stack = []

        for i in range(len(nums)):
            if nums[i] in stack:
                stack.remove(nums[i])
            else:
                stack.append(nums[i])

        return stack[0]
        