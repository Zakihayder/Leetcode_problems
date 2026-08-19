from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = defaultdict(int)

        for r, s in reservedSeats:
            rows[r] |= 1 << s

        ans = (n - len(rows)) * 2


        left = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)
        middle = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)
        right = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)

        for mask in rows.values():
            if (mask & left) == 0 and (mask & right) == 0:
                ans += 2

            elif ((mask & left) == 0 or
                  (mask & middle) == 0 or
                  (mask & right) == 0):
                ans += 1

        return ans