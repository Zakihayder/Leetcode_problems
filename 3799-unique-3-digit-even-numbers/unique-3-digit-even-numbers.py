class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = [0] * 10

        for d in digits:
            count[d] += 1

        ans = 0

        for a in range(1, 10):
            if count[a] == 0:
                continue

            count[a] -= 1

            for b in range(10):
                if count[b] == 0:
                    continue

                count[b] -= 1

                for c in range(0, 10, 2):
                    if count[c] > 0:
                        ans += 1

                count[b] += 1

            count[a] += 1

        return ans