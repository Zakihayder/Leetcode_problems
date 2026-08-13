class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:

        n = len(values)

        graph = [[] for _ in range(n)]

        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))

        visited = [0] * n
        visited[0] = 1

        ans = 0

        def dfs(node, time, quality):
            nonlocal ans

            if node == 0:
                ans = max(ans, quality)

            for nxt, cost in graph[node]:
                new_time = time + cost

                if new_time > maxTime:
                    continue

                if visited[nxt] == 0:
                    visited[nxt] = 1

                    dfs(
                        nxt,
                        new_time,
                        quality + values[nxt]
                    )

                    visited[nxt] = 0
                else:
                    dfs(nxt, new_time, quality)

        dfs(0, 0, values[0])

        return ans