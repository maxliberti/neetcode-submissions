class MinStack:

    import heapq

    def __init__(self):
        self.minStack = []
        self.minSoFar = []

    def push(self, val: int) -> None:
        self.minStack.append(val)
        if not self.minSoFar:
            self.minSoFar.append(val)
        else:
            res = min(self.minSoFar[-1], val)
            self.minSoFar.append(res)
            

    def pop(self) -> None:
        if self.minStack:
            self.minStack.pop()
            self.minSoFar.pop()

    def top(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        
    def getMin(self) -> int:
        if self.minSoFar:
            return self.minSoFar[-1]
        else:
            return 0
