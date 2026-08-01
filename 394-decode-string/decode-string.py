class Solution(object):
    def decodeString(self, s):
        count_stack = []
        string_stack = []
        curr = ""
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == "[":
                count_stack.append(num)
                string_stack.append(curr)
                curr = ""
                num = 0
            elif ch == "]":
                repeat = count_stack.pop()
                curr = string_stack.pop() + curr * repeat
            else:
                curr += ch

        return curr