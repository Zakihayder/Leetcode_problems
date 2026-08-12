class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 0:
            return 0

        if n <= 3:
            return 1

        s = [1, 2, 2]
        i = 2
        num = 1
        count = 1  # Number of 1s in [1,2,2]

        while len(s) < n:
            for _ in range(s[i]):
                s.append(num)

                if num == 1:
                    count += 1

                if len(s) == n:
                    break

            num = 3 - num  # 1 <-> 2
            i += 1

        return count