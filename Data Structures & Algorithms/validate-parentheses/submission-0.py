class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for ch in s:
            if ch == '[' or ch == '{' or ch == "(":
                stack.append(ch)
            
            elif c == ')' or ch == '}' or ch == ']':
                if not stack: return False

                top = stack[-1]

                if((ch == ')' and top == '(') or (ch == '}' and top == '{') or (ch == ']' and top == '[')):
                    return False

                stack.pop()

        return not stack

