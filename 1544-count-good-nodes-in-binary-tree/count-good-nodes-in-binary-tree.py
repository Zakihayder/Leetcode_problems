# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def goodNodes(self, root):
        self.ans = 0

        def dfs(node, mx):
            if not node:
                return

            if node.val >= mx:
                self.ans += 1
                mx = node.val

            dfs(node.left, mx)
            dfs(node.right, mx)

        dfs(root, float("-inf"))
        return self.ans