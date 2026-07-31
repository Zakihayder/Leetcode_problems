class Solution:
    def removeStars(self, s: str) -> str:
        string = ""
        string += s[0]
        for i in range(1,len(s)):
            if s[i] == '*':
                string = string[:-1]
            else:
                string += s[i]
        return string

        