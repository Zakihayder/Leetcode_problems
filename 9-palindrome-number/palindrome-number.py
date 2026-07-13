class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            string =str(x)
            length = len(string)

            for i in range(length/2):
                if string[i] != string[length-1-i]:
                    return False
            return True



        