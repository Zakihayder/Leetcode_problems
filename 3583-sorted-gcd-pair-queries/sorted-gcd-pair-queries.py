import bisect

class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        max_val = max(nums)

        # Step 1: count occurrences of each value
        cnt = [0] * (max_val + 1)
        for num in nums:
            cnt[num] += 1

        # Step 2: for each v, count how many numbers are divisible by v
        multiples = [0] * (max_val + 1)
        for v in range(1, max_val + 1):
            total = 0
            for m in range(v, max_val + 1, v):
                total += cnt[m]
            multiples[v] = total

        # Step 3: pairs where BOTH numbers divisible by v -> C(multiples[v], 2)
        # then subtract pairs whose gcd is actually a LARGER multiple of v,
        # to isolate pairs whose gcd is EXACTLY v
        gcd_count = [0] * (max_val + 1)
        for v in range(max_val, 0, -1):
            pairs = multiples[v] * (multiples[v] - 1) // 2
            for m in range(2 * v, max_val + 1, v):
                pairs -= gcd_count[m]
            gcd_count[v] = pairs

        # Step 4: build prefix sum -> prefix[v] = total pairs with gcd <= v
        prefix = [0] * (max_val + 1)
        prefix[1] = gcd_count[1]
        for v in range(2, max_val + 1):
            prefix[v] = prefix[v - 1] + gcd_count[v]

        # Step 5: answer each query via binary search on the prefix sum array
        result = []
        for q in queries:
            # find smallest v such that prefix[v] > q  (0-indexed queries)
            lo, hi = 1, max_val
            while lo < hi:
                mid = (lo + hi) // 2
                if prefix[mid] > q:
                    hi = mid
                else:
                    lo = mid + 1
            result.append(lo)

        return result