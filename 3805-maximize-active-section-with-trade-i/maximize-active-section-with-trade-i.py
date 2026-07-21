class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        t = '1' + s + '1'  
        n = len(t)
        ones = s.count('1')

        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and t[j] == t[i]:
                j += 1
            runs.append((t[i], j - i))
            i = j

        best_gain = 0
        
        for idx in range(1, len(runs) - 1):
            char, length = runs[idx]
            if char == '1':
                left_zeros = runs[idx - 1][1] if runs[idx - 1][0] == '0' else 0
                right_zeros = runs[idx + 1][1] if runs[idx + 1][0] == '0' else 0
                best_gain = max(best_gain, left_zeros + right_zeros)

        return ones + best_gain