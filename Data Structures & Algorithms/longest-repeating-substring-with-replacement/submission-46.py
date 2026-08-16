class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        fre = {}
        left = 0
        ml = 0
        mf = 0

        for right in range(len(s)):
            c = s[right]
            fre[c] = fre.get(c, 0) + 1

            mf = max(mf, fre[c])
            wl = right - left + 1
            v  = wl - mf

            while v > k:
                fre[s[left]] -= 1
                left += 1
                wl = right - left + 1
                v = wl - mf
            ml = max(ml, wl)
        return ml    
                
                
            
            
            
        