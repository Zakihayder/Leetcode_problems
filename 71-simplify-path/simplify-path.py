class Solution(object):
    def simplifyPath(self, path):
        stack = []
        parts = path.split('/')
        
        for part in parts:
            if part == '' or part == '.':
                continue  # skip empty strings (from //) and current-dir
            elif part == '..':
                if stack:
                    stack.pop()  # go up a directory, if possible
            else:
                stack.append(part)  # valid directory/file name
        
        return '/' + '/'.join(stack)