import heapq

class SmallestInfiniteSet(object):

    def __init__(self):
        self.curr = 1
        self.heap = []
        self.added = set()

    def popSmallest(self):
        if self.heap:
            x = heapq.heappop(self.heap)
            self.added.remove(x)
            return x

        self.curr += 1
        return self.curr - 1

    def addBack(self, num):
        if num < self.curr and num not in self.added:
            heapq.heappush(self.heap, num)
            self.added.add(num)