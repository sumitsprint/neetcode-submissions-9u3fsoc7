class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        need = {}
        min_length = float('inf')
        

        for n in t:
            need[n] = need.get(n, 0) + 1

        req = len(need)

        formed = 0

        left = 0

        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            if s[right] in need and window[s[right]] == need[s[right]]:

                formed += 1
            while formed == req:
                length = right - left + 1
                if length < min_length:
                    min_length = length
                    start = left
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    formed -= 1
                left += 1

        if min_length == float('inf'):
            return "" 
        return s[start:start+min_length]  






        