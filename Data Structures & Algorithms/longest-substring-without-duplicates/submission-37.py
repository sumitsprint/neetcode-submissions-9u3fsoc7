class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        see = set()
        ml = 0
        left = 0

        for i in range(len(s)):
            while s[i] in see:
                see.remove(s[left])
                left += 1

            see.add(s[i])

            ml = max(ml, i - left + 1)
        return ml
            



        
        
        
            

        