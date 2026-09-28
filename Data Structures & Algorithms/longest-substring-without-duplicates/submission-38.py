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
            #answer is recorded from valid state, never from a invalid state
            max_longest = max(max_longest, len(seen))
        return max_longest    


                

# tc O(n)
# sc O(min(n,m))
        
        