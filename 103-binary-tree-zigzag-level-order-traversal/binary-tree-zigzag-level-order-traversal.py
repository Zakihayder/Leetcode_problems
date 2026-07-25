from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        q = deque([root])
        ans = []

        leftToRight = True

        while q:
            size = len(q)
            level = [0] * size

            for i in range(size):
                node = q.popleft()

                index = i if leftToRight else size - 1 - i
                level[index] = node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans.append(level)
            leftToRight = not leftToRight

        return ans