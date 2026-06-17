class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:

        self.stack.append(val)
        if len(self.min_stack) > 0:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        top = self.stack.pop()
        self.stack.append(top)
        return top

    def getMin(self) -> int:
        print(self.min_stack)
        return self.min_stack[-1]
        
