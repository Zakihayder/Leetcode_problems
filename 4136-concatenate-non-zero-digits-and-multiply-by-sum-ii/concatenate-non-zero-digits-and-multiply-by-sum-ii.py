class Solution(object):
    def sumAndMultiply(self, s, queries):
        MOD = 10**9 + 7
        n = len(s)

        digits = []
        pos = []

        for i, ch in enumerate(s):
            if ch != '0':
                digits.append(int(ch))
                pos.append(i)

        m = len(digits)

        # prefix digit sums
        ps = [0] * (m + 1)
        for i in range(m):
            ps[i + 1] = ps[i] + digits[i]

        # powers of 10
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # prefix concatenated numbers
        pref = [0] * (m + 1)
        for i in range(m):
            pref[i + 1] = (pref[i] * 10 + digits[i]) % MOD

        # mapping arrays
        nextNZ = [-1] * n
        prevNZ = [-1] * n

        j = 0
        for i in range(n):
            while j < m and pos[j] < i:
                j += 1
            if j < m:
                nextNZ[i] = j

        j = m - 1
        for i in range(n - 1, -1, -1):
            while j >= 0 and pos[j] > i:
                j -= 1
            if j >= 0:
                prevNZ[i] = j

        ans = []

        for l, r in queries:
            L = nextNZ[l]
            R = prevNZ[r]

            if L == -1 or R == -1 or L > R:
                ans.append(0)
                continue

            digit_sum = ps[R + 1] - ps[L]

            length = R - L + 1
            x = (pref[R + 1] - pref[L] * pow10[length]) % MOD

            ans.append((x * digit_sum) % MOD)

        return ans