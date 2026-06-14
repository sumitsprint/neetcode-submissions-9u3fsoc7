class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_longest = 0
        left = 0
        
        for i in range(len(s)):
            
            while s[i] in seen:
                
                
                seen.remove(s[left])
                left += 1

            seen.add(s[i])
            max_longest = max(max_longest, len(seen))
        return max_longest    


                


        
        