class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:

        graph = [[] for _ in range(n)]
        reverse = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))
            reverse[v].append((u, w))

        def dijkstra(start, graph):
            INF = float('inf')
            dist = [INF] * n
            dist[start] = 0

            heap = [(0, start)]

            while heap:
                d, u = heapq.heappop(heap)

                if d > dist[u]:
                    continue

                for v, w in graph[u]:
                    nd = d + w

                    if nd < dist[v]:
                        dist[v] = nd
                        heapq.heappush(heap, (nd, v))

            return dist

        d1 = dijkstra(src1, graph)
        d2 = dijkstra(src2, graph)
        d3 = dijkstra(dest, reverse)

        ans = float('inf')

        for i in range(n):
            if d1[i] == float('inf'):
                continue
            if d2[i] == float('inf'):
                continue
            if d3[i] == float('inf'):
                continue

            ans = min(ans, d1[i] + d2[i] + d3[i])

        return -1 if ans == float('inf') else ans