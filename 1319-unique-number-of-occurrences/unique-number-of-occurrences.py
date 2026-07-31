class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr = Counter(arr)
        stack = []
        for start,end in arr.most_common():
            if end in stack:
                return False
            stack.append(end)
        return True

        