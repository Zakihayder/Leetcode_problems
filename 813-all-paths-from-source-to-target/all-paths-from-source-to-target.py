class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        result = []
        path = [0]

        def dfs(node):
            if node == target:
                result.append(path[:])
                return

            for nei in graph[node]:
                path.append(nei)
                dfs(nei)
                path.pop()

        dfs(0)
        return result