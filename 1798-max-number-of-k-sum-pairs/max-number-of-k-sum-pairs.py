class Solution(object):
    def maxOperations(self, nums, k):
        freq = {}
        ans = 0

        for num in nums:
            target = k - num

            if freq.get(target, 0):
                ans += 1
                freq[target] -= 1
            else:
                freq[num] = freq.get(num, 0) + 1

        return ans