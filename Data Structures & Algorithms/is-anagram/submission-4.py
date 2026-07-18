class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if lenth not same not anagram 
        if len(s) != len(t):
            return False
        # same same char if sorted = anagram ; otherwise not 
        return sorted(s) == sorted(t)
        