from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        LIMIT = 10**6 + 1

        cnt = Counter(s)
        half = {}
        mid = ""

        for c in sorted(cnt):
            half[c] = cnt[c] // 2
            if cnt[c] & 1:
                mid = c

        def ways(freq):
            total = sum(freq.values())
            res = 1
            rem = total
            for v in freq.values():
                if v:
                    res *= comb(rem, v)
                    if res > LIMIT:
                        return LIMIT
                    rem -= v
            return min(res, LIMIT)

        if ways(half) < k:
            return ""

        left = []
        m = sum(half.values())

        for _ in range(m):
            for ch in sorted(half):
                if half[ch] == 0:
                    continue

                half[ch] -= 1
                cnt_perm = ways(half)

                if cnt_perm >= k:
                    left.append(ch)
                    break

                k -= cnt_perm
                half[ch] += 1

        left = "".join(left)
        return left + mid + left[::-1]