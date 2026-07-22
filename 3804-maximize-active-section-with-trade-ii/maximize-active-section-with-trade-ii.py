class Group(object):
    __slots__ = ('start', 'length')

    def __init__(self, start, length):
        self.start = start
        self.length = length


class SparseTable(object):
    def __init__(self, nums):
        self.n = len(nums)
        levels = self.n.bit_length() + 1
        self.st = [[0] * (self.n + 1) for _ in range(levels)]
        if self.n > 0:
            self.st[0][:self.n] = nums
        for i in range(1, self.n.bit_length() + 1):
            for j in range(0, self.n - (1 << i) + 1):
                self.st[i][j] = max(self.st[i - 1][j],
                                     self.st[i - 1][j + (1 << (i - 1))])

    def query(self, l, r):
        """Returns max(nums[l..r]), inclusive."""
        length = r - l + 1
        i = length.bit_length() - 1
        return max(self.st[i][l], self.st[i][r - (1 << i) + 1])


class Solution(object):
    def maxActiveSectionsAfterTrade(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(s)
        ones = s.count('1')
        zero_groups, zero_group_index = self._get_zero_groups(s)

        if not zero_groups:
            return [ones] * len(queries)

        st = SparseTable(self._get_zero_merge_lengths(zero_groups))
        ans = []

        for l, r in queries:
            left = (-1 if zero_group_index[l] == -1 else
                    zero_groups[zero_group_index[l]].length -
                    (l - zero_groups[zero_group_index[l]].start))
            right = (-1 if zero_group_index[r] == -1 else
                     r - zero_groups[zero_group_index[r]].start + 1)

            end_group_index = (zero_group_index[r] if s[r] == '1'
                                else zero_group_index[r] - 1)
            start_adj_idx, end_adj_idx = self._map_to_adjacent_group_indices(
                zero_group_index[l] + 1, end_group_index)

            active_sections = ones

            if (s[l] == '0' and s[r] == '0' and
                    zero_group_index[l] + 1 == zero_group_index[r]):
                active_sections = max(active_sections, ones + left + right)
            elif start_adj_idx <= end_adj_idx:
                active_sections = max(
                    active_sections,
                    ones + st.query(start_adj_idx, end_adj_idx))

            if (s[l] == '0' and
                    zero_group_index[l] + 1 <= end_group_index):
                active_sections = max(
                    active_sections,
                    ones + left + zero_groups[zero_group_index[l] + 1].length)

            if s[r] == '0' and zero_group_index[l] < zero_group_index[r] - 1:
                active_sections = max(
                    active_sections,
                    ones + right + zero_groups[zero_group_index[r] - 1].length)

            ans.append(active_sections)

        return ans

    def _get_zero_groups(self, s):
        """Returns the zero groups and, for every index i, the index of the
        zero group i belongs to (or the most recent zero group seen so far
        if s[i] == '1')."""
        zero_groups = []
        zero_group_index = []

        for i, ch in enumerate(s):
            if ch == '0':
                if i > 0 and s[i - 1] == '0':
                    zero_groups[-1].length += 1
                else:
                    zero_groups.append(Group(i, 1))
            zero_group_index.append(len(zero_groups) - 1)  # unconditional, like the C++ version

        return zero_groups, zero_group_index

    def _get_zero_merge_lengths(self, zero_groups):
        """Returns the combined lengths of every pair of adjacent zero groups."""
        return [zero_groups[i].length + zero_groups[i + 1].length
                for i in range(len(zero_groups) - 1)]

    def _map_to_adjacent_group_indices(self, start_group_index, end_group_index):
        return start_group_index, end_group_index - 1