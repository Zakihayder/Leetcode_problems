from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        rows, cols = len(maze), len(maze[0])
        q = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while q:
            r, c, steps = q.popleft()

            if (r, c) != tuple(entrance) and (
                r == 0 or r == rows - 1 or c == 0 or c == cols - 1
            ):
                return steps

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < rows and 0 <= nc < cols and
                        maze[nr][nc] == '.'):
                    maze[nr][nc] = '+'
                    q.append((nr, nc, steps + 1))

        return -1