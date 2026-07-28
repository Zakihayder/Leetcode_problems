class Solution(object):
    def smallestPalindrome(self, s):
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        first = []
        middle = ""

        for i in range(26):
            if cnt[i] % 2:
                middle = chr(i + ord('a'))

            first.append(chr(i + ord('a')) * (cnt[i] // 2))

        first = "".join(first)
        return first + middle + first[::-1]