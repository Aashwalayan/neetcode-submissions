class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for e in tokens:
            if e not in '+/*-':
                stack.append(int(e))
            else:
                right = stack.pop()
                left = stack.pop()

                if e == '+':
                    stack.append(right + left)

                elif e == '-':
                    stack.append(left - right)

                elif e == '*':
                    stack.append(right * left)

                elif e == '/':
                    stack.append(left / right)

        return stack.pop()