class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        max_fre = 0
        left = 0
        fre = [0] * 26

        for right in range(len(s)):
            fre[ord(s[right]) - ord('A')] += 1
            max_fre = max(max_fre, fre[ord(s[right]) - ord('A')])
            window_length = right - left + 1
            validity = window_length - max_fre
            while validity > k and left < len(s):
                fre[ord(s[left]) - ord("A")] -= 1
                left += 1
                window_length = right - left +1
                
                
                
                validity = window_length - max_fre
            max_length = max(max_length, window_length)
        return max_length        
                



                








            
            



         




        

        