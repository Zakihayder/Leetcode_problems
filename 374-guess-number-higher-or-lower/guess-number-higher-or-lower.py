# The guess API is already defined for you.
# def guess(num):
#     # -1 if num is higher than the picked number
#     # 1 if num is lower than the picked number
#     # 0 if num is correct

class Solution(object):
    def guessNumber(self, n):
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            res = guess(mid)

            if res == 0:
                return mid
            elif res < 0:
                right = mid - 1
            else:
                left = mid + 1