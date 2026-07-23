class Solution(object):
    def averageOfLevels(self, root):
        sums = []
        counts = []

        def dfs(node, level):
            if not node:
                return

            if level == len(sums):
                sums.append(node.val)
                counts.append(1)
            else:
                sums[level] += node.val
                counts[level] += 1

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        return [float(s) / c for s, c in zip(sums, counts)]