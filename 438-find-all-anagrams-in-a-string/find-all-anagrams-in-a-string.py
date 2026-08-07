class Solution(object):
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []

        need = [0] * 26
        window = [0] * 26

        for c in p:
            need[ord(c) - ord('a')] += 1

        res = []
        k = len(p)

        for i, c in enumerate(s):
            window[ord(c) - ord('a')] += 1

            if i >= k:
                window[ord(s[i - k]) - ord('a')] -= 1

            if window == need:
                res.append(i - k + 1)

        return res