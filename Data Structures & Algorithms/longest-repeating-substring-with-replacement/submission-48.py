class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        fre = {}
        left = 0
        max_l = 0
        max_f = 0

        #bounded window

        for right in range(len(s)):
            c = s[right]
            fre[c] = fre.get(c, 0) + 1
            max_f = max(max_f, fre[c])

            window_l = right - left + 1
            valid = window_l - max_f

            while valid > k and left < len(s):
                c = s[left]
                fre[c] -= 1
                left += 1
               
                window_l = right - left + 1
                valid = window_l - max_f
            max_l = max(max_l, window_l)    
        return max_l    



        