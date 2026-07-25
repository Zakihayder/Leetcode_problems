from collections import deque

class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []

        q = deque([root])
        ans = []

        while q:
            level_size = len(q)

            for i in range(level_size):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                if i == level_size - 1:
                    ans.append(node.val)

        return ans