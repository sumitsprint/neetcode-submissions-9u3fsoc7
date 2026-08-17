class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        fre = [0] * 26
        left = 0

        for n in s1:
            fre[ord(n) - ord('a')] += 1

        for right in range(len(s2)):
            c = s2[right]
            fre[ord(c) - ord('a')] -= 1
            if right - left + 1 > len(s1):
                c = s2[left]
                fre[ord(c) - ord('a')] += 1
                left  += 1
            if right - left + 1 == len(s1):
                if all(f == 0 for f in fre):
                    return True
        return False            



