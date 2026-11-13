class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        fre = [0]  * 26
        left  = 0


        for s in s1:
            fre[ord(s) - ord('a')] += 1

        for right in range(len(s2)):
            fre[ord(s2[right]) - ord('a')] -= 1

            if right - left + 1 > len(s1):
                fre[ord(s2[left]) - ord('a')] += 1
                left += 1




            if right - left + 1 == len(s1):
                if all(f == 0 for f in fre):
                    return True
        return False            







        