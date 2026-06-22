class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        see = set()
    
        for right in range(len(s)):
            while s[right] in see:
                see.remove(s[left])
                left += 1

            see.add(s[right])
            max_length = max(max_length, right -left +1)
        return max_length    











        