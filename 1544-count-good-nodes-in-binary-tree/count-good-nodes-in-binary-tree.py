# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def goodNodes(self, root):
        def dfs(node, mx):
            if not node:
                return 0

            good = 1 if node.val >= mx else 0
            mx = max(mx, node.val)

            return good + dfs(node.left, mx) + dfs(node.right, mx)

        return dfs(root, float("-inf"))