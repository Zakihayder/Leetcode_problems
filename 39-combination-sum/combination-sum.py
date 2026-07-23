class Solution(object):
    def combinationSum(self, candidates, target):
        if min(candidates) > target:
            return []
        
        ans = []

        def backtrack(index,path,total):
            if total == target:
                ans.append(path[:])
                return

            if total > target or index == len(candidates):
                return 
                
            path.append(candidates[index])
            backtrack(index,path,total + candidates[index])
            path.pop()
            backtrack(index+1, path,total)

        backtrack(0,[],0)
        return ans


        