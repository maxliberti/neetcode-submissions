class MinStack:

    import heapq

    def __init__(self):
        self.minStack = []
        self.minSoFar = []

    def push(self, val: int) -> None:
        self.minStack.append(val)
        val = min(val, self.minSoFar[-1] if self.minSoFar else val)
        self.minSoFar.append(val)
            
    def pop(self) -> None:
        self.minStack.pop()
        self.minSoFar.pop()

    def top(self) -> int:
        return self.minStack[-1]
        
    def getMin(self) -> int:
        return self.minSoFar[-1]
