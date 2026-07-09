class Solution(object):
    def isPalindrome(self, s):
        s = "".join([i for i in s if i.isalnum()]).lower()

        if s == s[::-1]:
            return True
        else:
            return False
        