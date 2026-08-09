import heapq

class Solution(object):
    def isPossible(self, target):
        total = sum(target)

        heap = [-x for x in target]
        heapq.heapify(heap)

        while True:
            largest = -heapq.heappop(heap)
            rest = total - largest

            # Already reached [1, 1, ..., 1]
            if largest == 1 or rest == 1:
                return True

            # Impossible cases
            if rest == 0 or largest <= rest:
                return False

            previous = largest % rest

            if previous == 0:
                return False

            total = rest + previous
            heapq.heappush(heap, -previous)