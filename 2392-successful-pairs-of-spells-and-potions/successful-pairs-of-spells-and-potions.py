from bisect import bisect_left

class Solution(object):
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        m = len(potions)
        ans = []

        for spell in spells:
            idx = bisect_left(potions, (success + spell - 1) // spell)
            ans.append(m - idx)

        return ans