class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        import heapq
        heap = []
        eaten = 0
        n = len(apples)
        day = 0

        while day < n or heap:
            # Add today's apples.
            if day < n and apples[day] > 0:
                heapq.heappush(
                    heap,
                    (day + days[day], apples[day])
                )

            # Remove expired apples.
            while heap and heap[0][0] <= day:
                heapq.heappop(heap)

            # Eat one apple with the earliest expiry.
            if heap:
                expiry, count = heapq.heappop(heap)
                eaten += 1

                if count > 1:
                    heapq.heappush(heap, (expiry, count - 1))

            day += 1

        return eaten