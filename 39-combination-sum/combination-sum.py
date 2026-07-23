class Solution(object):
    def combinationSum(self, candidates, target):
        ans = []

        def backtrack(start, path, remain):
            if remain == 0:
                ans.append(path[:])
                return

            if remain < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])

                # i, not i+1, because we can reuse the same number
                backtrack(i, path, remain - candidates[i])

                path.pop()

        backtrack(0, [], target)
        return ans