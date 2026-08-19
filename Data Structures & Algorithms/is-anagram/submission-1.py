class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = {} # Hash map for string s
        t_dict = {} # hash map for string t

        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1 
        
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1

        for letter, count in s_dict.items():
            if t_dict.get(letter, 0) != count:
                return False    
        
        return True
