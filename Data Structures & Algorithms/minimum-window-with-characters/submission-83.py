class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        win = {}
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        req = len(need)

        left = 0
        formed = 0
        min_l = float('inf')

        for right in range(len(s)):
            c = s[right]
            win[c] = win.get(c, 0) + 1
            if c in need and win[c] == need[c]:
                formed += 1
            while formed == req:
                length = right - left + 1
                if length < min_l:
                    min_l = length
                    start = left

                c = s[left]
                win[c] -= 1
                
                if c in need and win[c] < need[c]:
                    formed -= 1
                left += 1    
        if min_l == float('inf'):
            return ""
        return s[start:start+min_l]                
            
                    








        