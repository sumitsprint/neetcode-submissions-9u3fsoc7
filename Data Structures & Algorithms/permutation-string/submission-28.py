class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            
            return False
        fre = [0] * 26
        left =  0

        window = len(s1)
      
       # Fre array of s1
        for i in range(len(s1)):
            fre[ord(s1[i]) - ord('a')] += 1

        # check the first window
        for i in range(window):
            fre[ord(s2[i]) - ord('a')] -= 1

        if all(f == 0 for f in fre):
            return True

        for right in range(window, len(s2)):

            # character entering the window
            fre[ord(s2[right]) - ord('a')] -= 1

            #character leaving the window
            fre[ord(s2[left]) - ord('a')] += 1

            left += 1
            if all(f == 0 for f in fre):
                return True
                
        return False    











        
        