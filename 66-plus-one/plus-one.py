class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)

        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0  # carry: this digit becomes 0, continue to next

        # if we exit the loop, every digit was 9 (e.g. [9,9,9] -> [1,0,0,0])
        digits.insert(0, 1)
        return digits