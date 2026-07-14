class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = ['+', '-', '*', '/']

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            elif token in operators:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == '+':
                    res = operand1 + operand2
                elif token == '-':
                    res = operand1 - operand2
                elif token == '*':
                    res = operand1 * operand2
                elif token == '/':
                    res = int(operand1/operand2)
                stack.append(res)  
        return int(stack[-1])       







