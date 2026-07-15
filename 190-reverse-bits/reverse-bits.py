class Solution(object):
    def reverseBits(self, n):
        string = ""
        
        # FIX 1: use `n > 0` — `n > 1` was dropping the last bit
        while n > 0:
            if n % 2 == 0:
                string += "0"
            else:
                string += "1"
            n = n // 2

        # FIX 2: pad to exactly 32 bits, not multiples of 8
        while len(string) < 32:
            string += "0"

        # `string` now holds bits from LSB to MSB (string[0] = original bit 0)
        # FIX 3: to REVERSE, bit at position i must land at position (31 - i)
        # in the final integer — not stay at weight 2^i
        total = 0
        for i in range(32):
            total += (2 ** (31 - i)) * int(string[i])

        return total