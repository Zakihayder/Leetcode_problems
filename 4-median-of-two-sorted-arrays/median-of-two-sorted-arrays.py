class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        for i in range(len(nums2)):
            nums1.append(nums2[i])

        nums1.sort()
        print(nums1)
        if len(nums1)%2 == 0:
            return float(nums1[len(nums1)//2]+nums1[len(nums1)//2-1])/2.0
        else:
            return nums1[len(nums1)//2]
        