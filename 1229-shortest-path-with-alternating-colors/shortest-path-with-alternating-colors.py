class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        graph = [[] for _ in range(n)]

        for u, v in redEdges:
            graph[u].append((v, 0))

        for u, v in blueEdges:
            graph[u].append((v, 1))

        visited = [[False] * 2 for _ in range(n)]

        q = deque([
            (0, 0),
            (0, 1)
        ])

        visited[0][0] = True
        visited[0][1] = True

        ans = [-1] * n
        ans[0] = 0

        distance = 0

        while q:
            for _ in range(len(q)):
                node, last_color = q.popleft()

                next_color = 1 - last_color

                for nei, color in graph[node]:
                    if color != next_color:
                        continue

                    if visited[nei][color]:
                        continue

                    visited[nei][color] = True
                    q.append((nei, color))

                    if ans[nei] == -1:
                        ans[nei] = distance + 1

            distance += 1

        return ans