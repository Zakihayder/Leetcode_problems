class Solution(object):
    def maxPathSum(self, root):
        ans = [float("-inf")]

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if left < 0:
                left = 0
            if right < 0:
                right = 0

            total = node.val + left + right
            if total > ans[0]:
                ans[0] = total

            return node.val + (left if left > right else right)

        dfs(root)
        return ans[0]