class Solution(object):
    def calculate(self, s):
        stack = []
        result = 0      
        num = 0         
        sign = 1        

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            
            elif char in '+-':
                result += sign * num 
                num = 0
                sign = 1 if char == '+' else -1
            
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                
                result = 0
                sign = 1
            
            elif char == ')':
                result += sign * num   # apply last number before closing
                num = 0
                # pop sign and previous result, combine
                result *= stack.pop()  # this is the sign before '('
                result += stack.pop()  # this is the result before '('
        
        result += sign * num  # apply the final number
        return result