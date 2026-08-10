class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        minimum = float('inf')
        ans = []

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]

            if diff < minimum:
                minimum = diff
                ans = [[arr[i - 1], arr[i]]]

            elif diff == minimum:
                ans.append([arr[i - 1], arr[i]])

        return ans