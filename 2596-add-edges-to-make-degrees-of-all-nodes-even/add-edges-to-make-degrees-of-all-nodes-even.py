class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        graph = [set() for _ in range(n + 1)]

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        odd = [i for i in range(1, n + 1) if len(graph[i]) % 2]

        if not odd:
            return True

        if len(odd) not in (2, 4):
            return False

        if len(odd) == 2:
            a, b = odd

            if b not in graph[a]:
                return True

            for x in range(1, n + 1):
                if x != a and x != b:
                    if x not in graph[a] and x not in graph[b]:
                        return True

            return False

        a, b, c, d = odd

        return (
            (b not in graph[a] and d not in graph[c]) or
            (c not in graph[a] and d not in graph[b]) or
            (d not in graph[a] and c not in graph[b])
        )