class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_l = 0
        n = len(s)
        fre =[0] * 26
        max_f = 0
        
        for i in range(n):
            fre[ord(s[i]) - ord('A')] += 1

            window_l = i - left + 1

            max_f = max(max_f ,fre[ord(s[i]) - ord("A")])

            validity = window_l - max_f

            while validity > k and left < n:
                fre[ord(s[left]) - ord("A")] -= 1
                left += 1
                window_l = i - left  +1
                
                validity = window_l - max_f
            max_l = max(max_l, window_l)
        return max_l        


            


        