class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = {}

        for n in s1:
            need[n] = need.get(n, 0) + 1

        left = 0
        win = {}

        for right in range(len(s2)):
            win[s2[right]] = win.get(s2[right], 0) + 1

            if right - left + 1 > len(s1):
                win[s2[left]] -= 1
                if win[s2[left]] == 0:
                    del win[s2[left]]
                left += 1

            if win == need:
                return True
        return False            


        