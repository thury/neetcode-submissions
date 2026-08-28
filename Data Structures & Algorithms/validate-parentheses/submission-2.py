class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')':'(', '}':'{', ']':'['}
        for c in s:
            # abre
            if c in brackets.values():
                stack.append(c)
                continue
            #cierra
            if len(stack) == 0:
                return False
            if brackets[c] != stack.pop():
                return False
        return len(stack) == 0
            
        