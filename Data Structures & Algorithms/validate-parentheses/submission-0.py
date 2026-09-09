class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for char in s:
            if char in '{([':
                stack.append(char)

            elif char in '})]':
                if len(stack) == 0:
                    return False
                
                if stack.pop() != pairs[char]:
                    return False
        return len(stack) == 0