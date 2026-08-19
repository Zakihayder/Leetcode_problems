class Solution:
    def countAndSay(self, n: int) -> str:
        rle = "1"

        for _ in range(n - 1):
            result = []
            i = 0

            while i < len(rle):
                j = i

                while j < len(rle) and rle[j] == rle[i]:
                    j += 1

                result.append(str(j - i))
                result.append(rle[i])

                i = j

            rle = "".join(result)
        return rle
