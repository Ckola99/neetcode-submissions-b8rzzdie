class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
                print(f'addition happened current stack {stack}')
            elif token == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b) - int(a))
            elif token == '*':
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif token == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b) / int(a))
            else:
                stack.append(token)

        return int(stack[0])