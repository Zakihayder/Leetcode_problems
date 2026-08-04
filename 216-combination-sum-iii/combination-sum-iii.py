class Solution(object):
    def combinationSum3(self, k, n):
        ans = []

        def backtrack(start, total, path):
            if len(path) == k:
                if total == n:
                    ans.append(path[:])
                return

            for i in range(start, 10):
                if total + i > n:
                    break
                path.append(i)
                backtrack(i + 1, total + i, path)
                path.pop()

        backtrack(1, 0, [])
        return ans