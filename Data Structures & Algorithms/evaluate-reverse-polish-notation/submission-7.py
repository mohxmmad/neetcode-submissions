class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+": 
                a = stack[-1]
                stack.pop()
                b = stack[-1]
                stack.pop()
                res = int(a + b)
                stack.append(res)
            elif token == "-":
                a = stack[-1]
                stack.pop()
                b = stack[-1]
                stack.pop()
                res = int(b - a)
                stack.append(res)
            elif token == "*":
                a = stack[-1]
                stack.pop()
                b = stack[-1]
                stack.pop()
                res = int(a * b)
                stack.append(res)
            elif token == "/":
                a = stack[-1]
                stack.pop()
                b = stack[-1]
                stack.pop()
                if ( a != 0):
                    res = int(b / a)
                stack.append(res)
            else:
                val = int(token)
                stack.append(val)
        if len(stack) == 1:
            return stack[0]
        
        return 0