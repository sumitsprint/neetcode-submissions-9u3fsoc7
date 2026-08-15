class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_l = float('inf')

        fre = [0] * 26

        window = {}
        need = {}

        for n in t:
            need[n] = need.get(n, 0) + 1

        left = 0  
        formed = 0
        req = len(need)  

        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            if s[right] in need and window[s[right]] == need[s[right]]:
                formed += 1
            while formed == req:
                length = right - left + 1
                if length < min_l:
                    min_l = length
                    start = left
                
                window[s[left]] -= 1
                

                if s[left] in need and window[s[left]] < need[s[left]]:
                    formed -= 1
                left += 1
        if min_l == float('inf'):
            return ""         
                
        return s[start:start+min_l]        
                    
                
                    

            





        