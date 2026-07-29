class Solution(object):
    def compress(self, chars):
        i = 0
        write = 0
        n = len(chars)

        while i < n:
            ch = chars[i]
            count = 0

            while i < n and chars[i] == ch:
                i += 1
                count += 1

            chars[write] = ch
            write += 1

            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1

        return write