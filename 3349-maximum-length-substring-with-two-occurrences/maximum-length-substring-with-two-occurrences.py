class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = [0] * 26
        left = 0
        ans = 0

        for right in range(len(s)):
            idx = ord(s[right]) - ord('a')
            count[idx] += 1

            while count[idx] > 2:
                count[ord(s[left]) - ord('a')] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans