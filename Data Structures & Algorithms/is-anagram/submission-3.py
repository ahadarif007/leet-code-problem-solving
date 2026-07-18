class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if lenth not same not anagram 
        if len(s) != len(t):
            return False
        # same same char if sorted = anagram
        s1= sorted(s)
        t1 = sorted(t)
        return s1 == t1
        