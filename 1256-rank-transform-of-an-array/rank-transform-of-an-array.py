class Solution(object):
    def arrayRankTransform(self, arr):
        if not arr:
            return []
        
        sorted_unique = sorted(set(arr))
        
        rank = {val: i + 1 for i, val in enumerate(sorted_unique)}
        
        return [rank[num] for num in arr]