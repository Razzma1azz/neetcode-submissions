class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for c in s:
            if c in dict:
                if len(stack) == 0:
                    return False

                top = stack.pop()
                if top != dict[c]:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0