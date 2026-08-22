class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        while i < n and s[i] == ' ':
            i += 1

        sign = 1

        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        num = 0

        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')

            if num > 214748364 or (
                num == 214748364 and digit > 7
            ):
                return 2147483647 if sign == 1 else -2147483648

            num = num * 10 + digit
            i += 1

        return sign * num