class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        fre = [0] * 26
        max_length = 0
        max_fre = 0
        for right in range(len(s)):
            fre[ord(s[right]) - ord('A')] += 1
            max_fre = max(max_fre, fre[ord(s[right]) - ord('A')]) 
            window = right - left + 1
            

            valid = window - max_fre
            
            while valid > k and left < len(s):

                fre[ord(s[left]) - ord('A')] -= 1
                left += 1
                window = right - left + 1
                valid = window - max_fre
            max_length = max(max_length, window)
        return max_length        






            
            
        

        
        
        
        