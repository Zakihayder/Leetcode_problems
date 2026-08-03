from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxLevelSum(self, root):
        q = deque([root])
        level = 1
        ans = 1
        max_sum = float("-inf")

        while q:
            curr_sum = 0

            for _ in range(len(q)):
                node = q.popleft()
                curr_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if curr_sum > max_sum:
                max_sum = curr_sum
                ans = level

            level += 1

        return ans