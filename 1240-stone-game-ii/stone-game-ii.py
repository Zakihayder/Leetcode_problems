class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        memo = {}

        def dfs(i, M):
            if i >= n:
                return 0

            # Can take all remaining piles
            if i + 2 * M >= n:
                return suffix[i]

            key = (i, M)

            if key in memo:
                return memo[key]

            best = 0

            # Take X piles, where 1 <= X <= 2M
            for x in range(1, 2 * M + 1):
                # Opponent gets the best possible result
                opponent = dfs(i + x, max(M, x))

                # Current player's total
                current = suffix[i] - opponent

                best = max(best, current)

            memo[key] = best
            return best

        return dfs(0, 1)  