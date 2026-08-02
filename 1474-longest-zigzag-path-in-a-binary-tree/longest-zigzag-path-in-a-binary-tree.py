# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def longestZigZag(self, root):
        self.ans = 0

        def dfs(node, l, r):
            if not node:
                return

            self.ans = max(self.ans, l, r)

            dfs(node.left, r + 1, 0)
            dfs(node.right, 0, l + 1)

        dfs(root, 0, 0)
        return self.ans