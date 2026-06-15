class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = len(s)
        seen = set()
        left =0 
        l =0
        for i in range(x):
            while s[i] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[i])
            l = max(l, len(seen))
        return l    

        