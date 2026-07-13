class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        stack = [(root, root.val)]

        while stack:
            node, curr_sum = stack.pop()

            if not node.left and not node.right and curr_sum == targetSum:
                return True

            if node.left:
                stack.append((node.left, curr_sum + node.left.val))
            if node.right:
                stack.append((node.right, curr_sum + node.right.val))

        return False