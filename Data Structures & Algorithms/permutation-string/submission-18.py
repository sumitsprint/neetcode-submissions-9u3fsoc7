class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            
            return False
        fre = [0] * 26
        left = 0
        window_size = len(s1)

    
    
        for s in s1:
            fre[ord(s) - ord('a')] += 1
        
        right = 0    

        for i in range(window_size):

            fre[ord(s2[i]) - ord('a')] -= 1
        if all(f == 0 for f in fre):
                return True
        for right in range(window_size, len(s2)):
            fre[ord(s2[left]) - ord('a')] += 1
            left += 1
            fre[ord(s2[right]) - ord('a')] -= 1
            if all(f == 0 for f in fre):
                return True
        return False        




        

           
        





           



        
        

        

        