class Solution(object):
    def combinationSum(self, candidates, target):
        candidates.sort()
        ans = []

        def dfs(start, remain, path):
            if remain == 0:
                ans.append(path[:])
                return

            for i in range(start, len(candidates)):
                # No need to continue if candidate is too large
                if candidates[i] > remain:
                    break

                path.append(candidates[i])

                # Reuse the same number
                dfs(i, remain - candidates[i], path)

                path.pop()

        dfs(0, target, [])
        return ans