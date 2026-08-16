class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            
            return False
        fre = [0] * 26
        left =  0

       
       # Fre array of s1
        for i in range(len(s1)):
            fre[ord(s1[i]) - ord('a')] += 1

        # check the first window
        

        for right in range(len(s2)):

            # character entering the window
            fre[ord(s2[right]) - ord('a')] -= 1
            if right - left + 1 > len(s1):
                fre[ord(s2[left]) - ord('a')] += 1

                left += 1
            if right - left + 1 == len(s1):  
                if all(f == 0 for f in fre):
                    return True

        return False 
        