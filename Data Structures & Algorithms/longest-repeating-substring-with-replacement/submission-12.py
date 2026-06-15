class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        fre = [0] * 26
        left = 0
        max_freq = 0
        max_length = 0

        

        for right in range(len(s)):
            fre[ord(s[right]) - ord('A')] += 1
            max_freq = max(max_freq, fre[ord(s[right]) - ord('A')]) 
            window_length = right - left + 1
            
            validity = window_length - max_freq
            while validity > k and left < len(s):
                
                
                fre[ord(s[left]) - ord('A')] -= 1
                left += 1
                window_length = right - left + 1
                validity = window_length - max_freq
            max_length = max(window_length, max_length)    



        return max_length        




                


            

        



        
        