class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]

        for u, v, w in times:
            graph[u].append((v, w))

        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        heap = [(0, k)]

        while heap:
            time, node = heappop(heap)

            if time > dist[node]:
                continue

            for nei, weight in graph[node]:
                new_time = time + weight

                if new_time < dist[nei]:
                    dist[nei] = new_time
                    heappush(heap, (new_time, nei))

        ans = max(dist[1:])

        return -1 if ans == float('inf') else ans