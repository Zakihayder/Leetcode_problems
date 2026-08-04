class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(min(nums)+1,max(nums)):
            if i not in nums:
                arr.append(i)
        return arr