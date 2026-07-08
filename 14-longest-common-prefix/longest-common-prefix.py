class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = ""
        j = 0

        while True:
            for i in range(len(strs)):
                if j == len(strs[i]):
                    return prefix

            for i in range(len(strs) - 1):
                if strs[i][j] != strs[i + 1][j]:
                    return prefix

            prefix += strs[0][j]
            j += 1