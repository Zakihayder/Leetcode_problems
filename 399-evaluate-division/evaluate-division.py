from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)

        # Build graph
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1.0 / val

        def dfs(curr, target, visited):
            if curr == target:
                return 1.0

            visited.add(curr)

            for neighbor, weight in graph[curr].items():
                if neighbor not in visited:
                    result = dfs(neighbor, target, visited)
                    if result != -1.0:
                        return weight * result

            return -1.0

        ans = []

        for a, b in queries:
            if a not in graph or b not in graph:
                ans.append(-1.0)
            elif a == b:
                ans.append(1.0)
            else:
                ans.append(dfs(a, b, set()))

        return ans