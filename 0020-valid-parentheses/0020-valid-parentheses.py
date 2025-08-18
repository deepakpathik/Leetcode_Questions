class Solution:
    def isValid(self, s):
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '{':
                stack.append('}')
            elif c == '[':
                stack.append(']')
            elif stack and stack[-1] == c:
                stack.pop()
            else:
                return False
        return not stack
