class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        fre = [0] * 26
        fr = [0] * 26
        
        for c in s:
            fre[ord(c)-ord("a")] += 1
        for c in t:
            fr[ord(c)-ord('a')] += 1
        return fre == fr
        # tc - O(n)
        # sc-O(1)

           
                    
        
        