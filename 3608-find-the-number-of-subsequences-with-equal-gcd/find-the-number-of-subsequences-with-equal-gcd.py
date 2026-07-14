from collections import defaultdict

class Solution(object):
    def subsequencePairCount(self, nums):
        MOD = 10**9 + 7

        def my_gcd(a, b):
            # manual Euclidean algorithm — no library call
            while b:
                a, b = b, a % b
            return a

        dp = defaultdict(int)
        dp[(0, 0)] = 1

        for num in nums:
            new_dp = defaultdict(int)
            for (g1, g2), cnt in dp.items():
                # option 1: skip this number
                new_dp[(g1, g2)] = (new_dp[(g1, g2)] + cnt) % MOD

                # option 2: add to seq1
                ng1 = num if g1 == 0 else my_gcd(g1, num)
                new_dp[(ng1, g2)] = (new_dp[(ng1, g2)] + cnt) % MOD

                # option 3: add to seq2
                ng2 = num if g2 == 0 else my_gcd(g2, num)
                new_dp[(g1, ng2)] = (new_dp[(g1, ng2)] + cnt) % MOD

            dp = new_dp

        result = 0
        for (g1, g2), cnt in dp.items():
            if g1 == g2 and g1 > 0:
                result = (result + cnt) % MOD

        return result