class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution(object):
    def construct(self, grid):
        def build(r, c, size):
            first = grid[r][c]

            # Check if all values are the same
            same = True
            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != first:
                        same = False
                        break
                if not same:
                    break

            if same:
                return Node(first == 1, True, None, None, None, None)

            half = size // 2

            return Node(
                True,
                False,
                build(r, c, half),                    # Top Left
                build(r, c + half, half),             # Top Right
                build(r + half, c, half),             # Bottom Left
                build(r + half, c + half, half)       # Bottom Right
            )

        return build(0, 0, len(grid))