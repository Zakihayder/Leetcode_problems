from bisect import bisect_left

class Solution(object):
    def lengthOfLIS(self, nums):
        tails = []  # tails[k] = smallest possible tail value of an increasing subsequence of length k+1

        for num in nums:
            pos = bisect_left(tails, num)
            if pos == len(tails):
                tails.append(num)  # num extends the longest subsequence so far
            else:
                tails[pos] = num   # num can replace this position for a "better" (smaller) tail

        return len(tails)