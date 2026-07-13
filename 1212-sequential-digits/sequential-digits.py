class Solution(object):
    def sequentialDigits(self, low, high):
        
        digits = "123456789"
        result = []

        # try every possible length of sequential number (2 to 9 digits)
        for length in range(2, 10):
            for start in range(0, 10 - length):
                num = int(digits[start:start + length])
                if low <= num <= high:
                    result.append(num)

        return sorted(result)