class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])

        height = [[-1] * n for _ in range(m)]
        q = deque()

        for r in range(m):
            for c in range(n):
                if isWater[r][c] == 1:
                    height[r][c] = 0
                    q.append((r, c))

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    if height[nr][nc] == -1:
                        height[nr][nc] = height[r][c] + 1
                        q.append((nr, nc))

        return height