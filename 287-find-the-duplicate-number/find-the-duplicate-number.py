class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = Counter(nums)

        for i in nums.most_common():
            return i[0]
        