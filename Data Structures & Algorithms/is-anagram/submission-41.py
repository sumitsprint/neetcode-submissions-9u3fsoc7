class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fre = [0] * 26
        for c in s:
            fre[ord(c)-ord('a')] += 1

        for c in t:
            fre[ord(c)-ord('a')] -= 1

        return all(c==0 for c in fre)        
        