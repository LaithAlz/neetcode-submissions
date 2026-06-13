class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        total = 0
        if len(tokens) == 1:
            return int(tokens[0])
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                if len(stack) > 1:
                    num2 = stack.pop()
                    num1 = stack.pop()
                    print(num1, num2)
                    if token == "+":
                        total = num1 + num2
                    elif token == "-":
                        total = num1 - num2
                    elif token == "/":
                        total = int(num1 / num2)
                    elif token == "*":
                        total = num1 * num2
                    stack.append(total)
                    
                    
        return total
