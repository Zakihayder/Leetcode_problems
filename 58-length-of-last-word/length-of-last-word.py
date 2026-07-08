class Solution(object):
    def lengthOfLastWord(self, s):
        s = " ".join(s.split()[::-1])

        count = 0
        for i in s:
            if i != ' ':
                count += 1
            else:
                return count
        return count