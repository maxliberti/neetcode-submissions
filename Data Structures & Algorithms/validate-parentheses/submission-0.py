class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracks = {'}':'{', ']':'[', ')':'('}

        for c in s:
            if c in bracks: # if c is one of the keys, so closed bracket
                if stack and stack[-1] == bracks[c]: # if stack has values and the top of the stack is the matching closed bracket, pop stack
                    stack.pop()
                else:
                    return False # if c is one of the keys but its matching closing bracket isnt at the top of the stack return false
            else: # if its one of the values, its an open so append
                stack.append(c)
        
        return True if not stack else False
            