class Solution(object):
    def rearrangeSticks(self, n, k):
        MOD = 10**9 + 7

        dp = [0] * (k + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            new = [0] * (k + 1)

            for j in range(1, min(i, k) + 1):
                new[j] += dp[j - 1]

                new[j] += dp[j] * (i - 1)

                new[j] %= MOD

            dp = new

        return dp[k]