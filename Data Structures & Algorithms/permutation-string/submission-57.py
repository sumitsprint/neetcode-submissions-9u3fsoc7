class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False


        need = {

        }   

        for c in s1:
            need[c] = need.get(c, 0) + 1



        left = 0

        win = {}

        for right in range(len(s2)):
            c = s2[right]
            win[c] = win.get(c, 0) + 1
            if right - left + 1 > len(s1):
                c = s2[left]
                win[c] -= 1
                if win[c] == 0:
                    del win[c]
                left += 1
            if win == need:
                return True
        return False            


            
             