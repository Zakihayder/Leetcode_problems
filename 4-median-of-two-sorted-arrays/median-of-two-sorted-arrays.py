class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1 = sorted(nums1 + nums2)  
        n = len(nums1)

        if n % 2 == 0:
            return (nums1[n // 2] + nums1[n // 2 - 1]) / 2.0
        else:
            return float(nums1[n // 2])