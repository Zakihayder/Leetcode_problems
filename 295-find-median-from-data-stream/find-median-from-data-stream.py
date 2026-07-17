import heapq

class MedianFinder(object):

    def __init__(self):
        self.small = []  # max-heap (stored as negatives, since Python only has min-heap)
        self.large = []  # min-heap

    def addNum(self, num):
        # push to max-heap first (negate to simulate max-heap using heapq's min-heap)
        heapq.heappush(self.small, -num)

        # ensure every element in `small` is <= every element in `large`
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # rebalance sizes: `small` can have at most one more element than `large`
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]  # odd total count: middle element is top of `small`
        return (-self.small[0] + self.large[0]) / 2.0  # even: average of both tops