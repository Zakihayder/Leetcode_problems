class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7

        def dfs(node):
            if not node:
                return 0

            return node.val + dfs(node.left) + dfs(node.right)

        total = dfs(root)
        ans = 0

        def find(node):
            nonlocal ans

            if not node:
                return 0

            s = node.val + find(node.left) + find(node.right)

            ans = max(ans, s * (total - s))

            return s

        find(root)

        return ans % MOD