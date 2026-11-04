class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        fre = {}
        left = 0
        max_f = 0
        max_l = 0

        for right in range(len(s)):
            c = s[right]

            fre[c] = fre.get(c, 0) + 1
            max_f = max(max_f, fre.get(c))
            window = right - left + 1

            valid = window - max_f

            while valid > k:
                fre[s[left]] -= 1
                left += 1
                window = right - left + 1
                valid = window - max_f

                

            max_l = max(window, max_l)    
        return max_l    








        