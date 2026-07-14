from collections import defaultdict

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def my_gcd(a, b):
            # manual Euclidean algorithm, works for positive integers
            while b:
                a, b = b, a % b
            return a

        n = len(points)
        if n <= 2:
            return n

        max_count = 1

        for i in range(n):
            slopes = defaultdict(int)
            duplicates = 0
            x1, y1 = points[i]

            for j in range(n):
                if i == j:
                    continue
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1

                if dx == 0 and dy == 0:
                    duplicates += 1
                    continue

                if dx == 0:
                    slope = (1, 0)
                elif dy == 0:
                    slope = (0, 1)
                else:
                    g = my_gcd(abs(dx), abs(dy))
                    dx //= g
                    dy //= g
                    if dx < 0:
                        dx, dy = -dx, -dy
                    slope = (dx, dy)

                slopes[slope] += 1

            if slopes:
                max_count = max(max_count, max(slopes.values()) + duplicates + 1)
            else:
                max_count = max(max_count, duplicates + 1)

        return max_count