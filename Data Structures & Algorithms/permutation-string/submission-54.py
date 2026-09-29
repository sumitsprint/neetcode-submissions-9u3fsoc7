class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        need = {}

        for c in s1:
            need[c] = need.get(c, 0) + 1

        win = {}
        left = 0

        for right in range(len(s2)):
            c = s2[right]
            win[c] = win.get(c, 0) + 1

            #invalid window
            while right - left + 1 > len(s1):
                c1 = s2[left]
                win[c1] -= 1
                if win[c1] == 0:
                    del win[c1]
                left += 1
            if need == win:
                return True
        return False        



            

        