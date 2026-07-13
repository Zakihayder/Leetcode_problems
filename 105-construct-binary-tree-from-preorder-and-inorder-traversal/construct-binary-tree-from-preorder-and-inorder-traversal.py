class Solution(object):
    def buildTree(self, preorder, inorder):
        # map each value to its index in inorder, for O(1) lookups
        inorder_index = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0  

        def build(left, right):
            if left > right:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            # find where root splits the inorder range
            mid = inorder_index[root_val]


            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)