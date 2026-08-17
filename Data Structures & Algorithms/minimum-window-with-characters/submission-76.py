class Solution:
    def minWindow(self, s: str, t: str) -> str:
        formed = 0
        need = {}
        win = {}
        min_l = float('inf')

        for n in t:
            need[n] = need.get(n, 0) + 1



        req = len(need)

        left = 0

        for right in range(len(s)):
            c = s[right]
            win[c] = win.get(c, 0) + 1
            if c in need and win[c] == need[c]:
                formed += 1

                while formed == req:
                    l = right - left + 1
                    if l < min_l:
                        min_l = l
                        start = left
                    win[s[left]] -= 1
                       
                    
                    if s[left] in need and need[s[left]] > win[s[left]]:
                        formed -= 1
                    
                    left += 1 

        if min_l == float('inf'):
            return ""

        return s[start:start+min_l]                    
                    

                    



