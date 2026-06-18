class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        win = {}
        left = 0
        start = 0
        
        for i in t:
            need[i] = need.get(i, 0) + 1

        req = len(need)
        formed = 0
        cwl = float('inf')

        for i in range(len(s)):
            win[s[i]] = win.get(s[i], 0) + 1
            if s[i] in need:
                
                if win[s[i]] == need[s[i]]:
                    formed += 1
            while formed == req:
                if i - left + 1 < cwl:
                    cwl = i -left + 1
                    start = left
                
                ch = s[left]
                win[ch] -= 1
                if ch in need:
                    if win[ch] < need[ch]:
                        formed -= 1
                    
                left += 1
        if cwl == float('inf'):
            return ""        
        return s[start:start + cwl]            













        
        
        