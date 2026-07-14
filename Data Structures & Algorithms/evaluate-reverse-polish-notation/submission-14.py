class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        
        stack = []

        operators = ['+', '-', '*', '/']

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
                print(stack)
            elif token in operators:
                print(stack)
                operand2 = stack.pop()
                print(stack)
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
                print(stack)
        return int(stack[-1])       







