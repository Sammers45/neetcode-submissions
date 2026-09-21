class Solution:
    def isPalindrome(self, s: str) -> bool:
        character = []

        for l in s:
            if l.isalnum():
                character.append(l.lower())
        
        L = 0
        R = len(character) - 1

        while L < R:    
            if character[L] != character[R]:
                return False
            L += 1
            R -= 1
        return True