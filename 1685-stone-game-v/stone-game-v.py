from functools import cache
from itertools import accumulate

class Solution:
    def stoneGameV(self, stoneValue):
        prefix = list(accumulate(stoneValue, initial=0))

        @cache
        def dfs(left, right):
            if left >= right:
                return 0

            ans = 0
            left_sum = 0
            right_sum = prefix[right + 1] - prefix[left]

            for k in range(left, right):
                left_sum += stoneValue[k]
                right_sum -= stoneValue[k]

                if left_sum < right_sum:
                    if ans >= left_sum * 2:
                        continue

                    ans = max(ans, left_sum + dfs(left, k))

                elif left_sum > right_sum:
                    if ans >= right_sum * 2:
                        break

                    ans = max( ans, right_sum + dfs(k + 1, right))

                else:
                    ans = max( ans,left_sum + dfs(left, k), right_sum + dfs(k + 1, right))

            return ans

        return dfs(0, len(stoneValue) - 1)