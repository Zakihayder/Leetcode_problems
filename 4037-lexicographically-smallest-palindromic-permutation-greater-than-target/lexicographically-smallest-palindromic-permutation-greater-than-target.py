class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        odd = 0
        middle = ""

        for i in range(26):
            if cnt[i] % 2:
                odd += 1
                middle = chr(i + 97)

        if odd > 1:
            return ""

        half = [x // 2 for x in cnt]
        h = n // 2

        def build(left):
            right = left[::-1]
            if n % 2:
                return left + middle + right
            return left + right

        available = half[:]
        left = []
        possible = True

        for i in range(h):
            x = ord(target[i]) - 97

            if available[x] == 0:
                possible = False
                break

            available[x] -= 1
            left.append(target[i])

        if possible:
            candidate = build(''.join(left))

            if candidate > target:
                return candidate

       
        for i in range(h - 1, -1, -1):

            available = half[:]
            valid = True

            for j in range(i):
                x = ord(target[j]) - 97

                if available[x] == 0:
                    valid = False
                    break

                available[x] -= 1

            if not valid:
                continue

            target_char = ord(target[i]) - 97

            for x in range(target_char + 1, 26):
                if available[x] == 0:
                    continue

                available[x] -= 1

                suffix = []

                for c in range(26):
                    if available[c]:
                        suffix.append(chr(c + 97) * available[c])

                left_part = (
                    target[:i]
                    + chr(x + 97)
                    + ''.join(suffix)
                )

                candidate = build(left_part)

                if candidate > target:
                    return candidate

                available[x] += 1

        return ""