class Solution:
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        # 1. Store index-value pairs and sort them based on values
        pairs = sorted((x, i) for i, x in enumerate(nums))
        
        m = 20
        # f[i][k] stores the index reached from node i after 2^k transitions
        f = [[0] * m for _ in range(n)]
        
        # 2. Sliding window to find greedy maximal jumps to the right
        r = n - 1
        for l in range(n - 1, -1, -1):
            while pairs[r][0] - pairs[l][0] > maxDiff:
                r -= 1
            i, j = pairs[l][1], pairs[r][1]
            f[i][0] = j
            
            # 3. Populate binary lifting transitions for this index
            for k in range(1, m):
                f[i][k] = f[f[i][k - 1]][k - 1]
                
        ans = []
        # 4. Resolve queries using Binary Lifting
        for i, j in queries:
            if nums[i] > nums[j]:
                i, j = j, i
                
            if i == j:
                ans.append(0)
                continue
                
            if nums[i] == nums[j]:
                ans.append(1)
                continue
                
            d = 0
            for k in range(m - 1, -1, -1):
                if nums[f[i][k]] < nums[j]:
                    d |= 1 << k
                    i = f[i][k]
                    
            if nums[f[i][0]] < nums[j]:
                ans.append(-1)
            else:
                ans.append(d + 1)
                
        return ans
