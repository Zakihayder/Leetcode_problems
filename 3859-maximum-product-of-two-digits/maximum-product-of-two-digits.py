class Solution(object):
    def maxProduct(self, n):
        arr = []
        while n > 0:
            arr.append(n%10)
            n = n//10
        maximum = max(arr)
        arr.remove(maximum)
        return maximum * max(arr)
        