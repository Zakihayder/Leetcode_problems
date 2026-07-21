class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = '1' + s + '1'
        n = len(t)
        ones = s.count('1')

        best_gain = 0

        # rolling window of the last two COMPLETED runs (no list stored!)
        prev_char, prev_len = None, 0     # the run just before the current one
        prev2_char, prev2_len = None, 0   # the run before THAT

        i = 0
        while i < n:
            j = i
            while j < n and t[j] == t[i]:
                j += 1
            cur_char, cur_len = t[i], j - i

            # if the run we're about to "close out" the window on is:
            # prev2 = '0', prev = '1', cur = '0'  -> valid trade candidate
            if prev_char == '1' and prev2_char == '0' and cur_char == '0':
                best_gain = max(best_gain, prev2_len + cur_len)

            # slide the window forward by one run
            prev2_char, prev2_len = prev_char, prev_len
            prev_char, prev_len = cur_char, cur_len
            i = j

        return ones + best_gain