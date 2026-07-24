class Solution(object):
    def uniqueXorTriplets(self, nums):
        MAX = 2048

        pair = [False] * MAX

        for j in range(len(nums)):
            for k in range(j, len(nums)):
                pair[nums[j] ^ nums[k]] = True

        ans = [False] * MAX

        # Combine with every i
        for x in nums:
            for v in range(MAX):
                if pair[v]:
                    ans[x ^ v] = True

        return sum(ans)