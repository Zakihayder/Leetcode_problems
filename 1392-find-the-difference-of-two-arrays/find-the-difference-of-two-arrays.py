class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        nums1 = Counter(nums1)
        nums2 = Counter(nums2)

        ans = []
        answer = []

        for start,end in nums1.items():
            if start not in nums2:
                answer.append(start)
        
        ans.append(list(answer))
        answer = []

        for start,end in nums2.items():
            if start not in nums1:
                answer.append(start)
                
        ans.append(list(answer))
        return ans
        