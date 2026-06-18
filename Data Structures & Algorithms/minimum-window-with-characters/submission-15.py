class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        need = {}


        for n in t:
            need[n] = need.get(n, 0) + 1

        req = len(need)
        formed = 0
        min_length = float('inf')
        left = 0

        #expand until valid
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            if s[right] in need:
                if window[s[right]] == need[s[right]]:
                    formed += 1

            #shrink while valid
            while formed == req:
                length = right - left + 1
                if length < min_length:
                    min_length = length
                    #pre decrement value of left for valid window 
                    start = left
            
            
                window[s[left]] = window.get(s[left], 0) - 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    
                    formed -= 1
                #if formed has decremented now lwft will move to start of invalid window    
                left += 1
                
        if min_length == float('inf'):
            return ""  
        
        return s[start:start+min_length]         

                
                        








            

        