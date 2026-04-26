class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fre = [0] * 26
        for n in s:
            fre[ord(n) - ord('a')] += 1
        for n in t:  
            fre[ord(n) - ord('a')] -= 1  
        return all(f == 0 for f in fre)    
            
        
        