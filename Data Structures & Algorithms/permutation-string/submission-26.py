class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        fre = [0] * 26

      # fre of s1
        for n in s1:
            fre[ord(n) - ord('a')] += 1

        win_size = len(s1)


        for i in range(win_size):
            fre[ord(s2[i]) - ord('a')] -= 1

        if all(f == 0 for f in fre):
            return True

        left = 0
        for right in range(win_size, len(s2)):
            fre[ord(s2[left]) - ord('a')] += 1
            left += 1

            fre[ord(s2[right]) - ord('a')] -= 1

            if all(f == 0 for f in fre):
                return True

        return False    
            






        