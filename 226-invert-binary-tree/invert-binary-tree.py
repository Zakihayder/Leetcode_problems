class Solution(object):
    def invertTree(self, root):
        if not root:
            return None

        # swap left and right children
        root.left, root.right = root.right, root.left

        # recursively invert both subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root