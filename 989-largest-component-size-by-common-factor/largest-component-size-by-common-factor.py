from typing import List

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        max_num = max(nums)

        # SPF: smallest prime factor
        spf = list(range(max_num + 1))

        for i in range(2, int(max_num ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, max_num + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        parent = list(range(n))
        size = [1] * n

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            a = find(a)
            b = find(b)

            if a == b:
                return

            if size[a] < size[b]:
                a, b = b, a

            parent[b] = a
            size[a] += size[b]

        # prime factor -> index of first number containing it
        owner = {}

        for i, num in enumerate(nums):
            x = num

            while x > 1:
                p = spf[x]

                if p in owner:
                    union(i, owner[p])
                else:
                    owner[p] = i

                # Remove all occurrences of p
                while x % p == 0:
                    x //= p

        return max(size[find(i)] for i in range(n))