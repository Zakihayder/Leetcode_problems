from collections import Counter

class Solution(object):
    def closeStrings(self, word1, word2):
        c1 = Counter(word1)
        c2 = Counter(word2)

        return set(c1) == set(c2) and sorted(c1.values()) == sorted(c2.values())