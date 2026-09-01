class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                b = int(stack.pop())
                a = int(stack.pop())
                if token == "+":
                    stack.append(a + b)
                if token == "-":
                    stack.append(a - b)
                if token == "*":
                    stack.append(a * b)
                if token == "/":
                    stack.append(int(a / b))

            else:
                stack.append(token)

        return stack[-1]