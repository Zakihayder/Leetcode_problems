from collections import deque

class Solution(object):
    def averageOfLevels(self, root):
        q = deque([root])
        ans = []

        while q:
            level_size = len(q)
            total = 0

            for _ in range(level_size):
                node = q.popleft()
                total += node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            ans.append(float(total) / level_size)

        return ans