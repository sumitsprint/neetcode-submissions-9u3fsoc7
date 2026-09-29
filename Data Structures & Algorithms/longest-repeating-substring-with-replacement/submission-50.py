class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m = {}
        ml = 0
        
        left = 0    
        mf = 0


        for right in range(len(s)):
            c = s[right]
            m[c] = m.get(c, 0) + 1
            mf = max(m[c],mf)
            wl = right -left + 1
            valid = wl - mf

            while valid > k:
                m[s[left]] -= 1
                left += 1
                wl = right - left + 1
                
                valid = wl - mf



            ml = max(ml, wl)    
        return ml    


            



        