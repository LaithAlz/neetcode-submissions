class MinStack:

    def __init__(self):
        self.stack = []
        self.smallest = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.smallest) > 0:
            self.smallest.append(min(val, self.smallest[-1]))
        else:
            self.smallest.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        self.smallest.pop()
        return
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.smallest[-1]
            
