class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:

        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            a = find(a)
            b = find(b)

            if a == b:
                return

            if rank[a] < rank[b]:
                a, b = b, a

            parent[b] = a

            if rank[a] == rank[b]:
                rank[a] += 1

        ans = []

        for u, v in requests:
            ru = find(u)
            rv = find(v)

            # Already in the same component
            if ru == rv:
                ans.append(True)
                continue

            allowed = True

            # Check every restriction
            for x, y in restrictions:
                rx = find(x)
                ry = find(y)

                # Merging ru and rv would put
                # x and y into the same component.
                if (ru == rx and rv == ry) or \
                   (ru == ry and rv == rx):
                    allowed = False
                    break

            if allowed:
                union(ru, rv)
                ans.append(True)
            else:
                ans.append(False)

        return ans