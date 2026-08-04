from collections import defaultdict

class Solution(object):
    def minReorder(self, n, connections):
        graph = defaultdict(list)

        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))

        visited = [False] * n

        def dfs(city):
            visited[city] = True
            changes = 0

            for nei, cost in graph[city]:
                if not visited[nei]:
                    changes += cost + dfs(nei)

            return changes

        return dfs(0)