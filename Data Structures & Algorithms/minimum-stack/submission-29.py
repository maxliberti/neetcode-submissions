class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mins:
            if val <= self.mins[-1]:
                self.mins.append(val)
        else:
            self.mins.append(val)

    def pop(self) -> None:
        popped = self.stack[-1]
        del self.stack[-1]
        if self.mins:
            if popped == self.mins[-1]:
                self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        if self.mins:
            return self.mins[-1]
        else:
            return 0