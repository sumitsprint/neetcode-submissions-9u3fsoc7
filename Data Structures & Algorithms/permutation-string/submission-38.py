class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        fre = [0] * 26
        left = 0
        window = len(s1)
        

        for n in s1:
            fre[ord(n) - ord('a')] += 1

        for i in range(window):
            fre[ord(s2[i]) - ord('a')] -= 1

        if all(f == 0 for f in fre):
            return True

        for i in range(window, len(s2)):
            #enter
            fre[ord(s2[i]) - ord('a')] -= 1

            #leave
            fre[ord(s2[left]) - ord('a')] += 1
            left += 1
            if all(f == 0 for f in fre):
                return True
        return False        





            
            


            
                