class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:

        num = k
        if k not in nums:
            return k
            
        while k in nums:
            k += num

        return k 
        