class MedianFinder(object):

    def __init__(self):
        self.arr = []

    def addNum(self, num):
        self.arr.append(num)

    def findMedian(self):
        self.arr.sort()  
        n = len(self.arr)
        mid = n // 2

        if n % 2 == 1:
            return self.arr[mid]  # odd length: middle element
        else:
            return (self.arr[mid - 1] + self.arr[mid]) / 2.0  # even length: average of two middle elements