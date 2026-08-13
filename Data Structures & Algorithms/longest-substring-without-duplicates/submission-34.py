class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        see = set()
        ls = 0
        left = 0

        for i in range(len(s)):
    
                
            while s[i] in see:
                see.remove(s[left])
                left += 1

            see.add(s[i])
            cl = len(see)
            ls = max(ls, cl)
        return ls            



        

        