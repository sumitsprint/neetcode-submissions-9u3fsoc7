class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        fre = [0] * 26

        left  = 0
        max_fre = 0
        max_l = 0

        for right in range(len(s)):
            fre[ord(s[right]) - ord('A')] += 1
            max_fre = max(max_fre, fre[ord(s[right]) - ord('A')])
            length = right - left + 1

            while length - max_fre > k and left <len(s):
                fre[ord(s[left]) - ord('A')] -= 1
                # max(max_fre, fre[ord(s[left]) - ord('A')])

                left += 1
                length = right - left + 1

            max_l = max(max_l, length)

        return max_l        





            



        
        
        
        