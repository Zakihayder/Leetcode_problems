class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        def LCA(node):
            if not node or node == p or node == q:
                return node

            left = LCA(node.left)
            right = LCA(node.right)

            if left and right:
                return node

            return left if left else right

        return LCA(root)