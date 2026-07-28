class Solution(object):
    def mergeAlternately(self, word1, word2):
        ans = []
        i = j = 0

        while i < len(word1) and j < len(word2):
            ans.append(word1[i])
            ans.append(word2[j])
            i += 1
            j += 1

        ans.extend(word1[i:])
        ans.extend(word2[j:])

        return "".join(ans)