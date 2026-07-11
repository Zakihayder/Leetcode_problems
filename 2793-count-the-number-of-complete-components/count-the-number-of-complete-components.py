class Solution:
    def countCompleteComponents(self, n, edges):
        parent = list(range(n))
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
        
        for a, b in edges:
            union(a, b)
        
        node_count = defaultdict(int)
        edge_count = defaultdict(int)
        
        for i in range(n):
            node_count[find(i)] += 1
        for a, b in edges:
            edge_count[find(a)] += 1
        
        result = 0
        for root in node_count:
            V = node_count[root]
            E = edge_count[root]
            if E == V * (V - 1) // 2:
                result += 1
        
        return result