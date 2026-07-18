class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # same same char = anagram
        s1= sorted(s)
        t1 = sorted(t)
        return s1 == t1
        