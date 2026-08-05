# The guess API is already defined for you.
# def guess(num):
#     # return -1 if num is higher than the picked number
#     # return 1 if num is lower than the picked number
#     # return 0 if num is correct

class Solution(object):
    def guessNumber(self, n):
        left, right = 1, n

        while left <= right:
            mid = left + (right - left) // 2

            if guess(mid) == 0:
                return mid
            elif guess(mid) < 0:
                right = mid - 1
            else:
                left = mid + 1