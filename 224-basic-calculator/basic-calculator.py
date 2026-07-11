class Solution(object):
    def calculate(self, s):
        self.i = 0  # pointer into the string

        def helper():
            result = 0
            num = 0
            sign = 1

            while self.i < len(s):
                char = s[self.i]

                if char.isdigit():
                    num = num * 10 + int(char)
                elif char in '+-':
                    result += sign * num
                    num = 0
                    sign = 1 if char == '+' else -1
                elif char == '(':
                    self.i += 1
                    num = helper()  # recursively evaluate the sub-expression
                elif char == ')':
                    result += sign * num
                    return result

                self.i += 1

            result += sign * num
            return result

        return helper()