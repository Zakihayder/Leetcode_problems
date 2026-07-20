class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged = sorted(nums1 + nums2)  
        n = len(merged)

        if n % 2 == 0:
            return (merged[n // 2] + merged[n // 2 - 1]) / 2.0
        else:
            return float(merged[n // 2])