class Solution:
    def isValid(self, s: str) -> bool:         
        stack = []

        close_to_open = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c in close_to_open.values():
                stack.append(c)
            elif c in close_to_open.keys():
                if stack:
                    if stack[-1] == close_to_open[c]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                return False
        return False if stack else True