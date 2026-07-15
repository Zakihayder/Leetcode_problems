class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""

        start, max_len = 0, 1

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
           
            return right - left - 1, left + 1

        for i in range(len(s)):

            len1, start1 = expand(i, i)
            if len1 > max_len:
                max_len = len1
                start = start1

            len2, start2 = expand(i, i + 1)
            if len2 > max_len:
                max_len = len2
                start = start2

        return s[start:start + max_len]