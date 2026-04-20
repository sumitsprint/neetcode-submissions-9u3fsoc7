class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        fre = [0] * 26

        for n in s:
            fre[ord(n) - ord('a')] += 1
        for m in t:
            fre[ord(m) - ord('a')] -= 1

        return all(f == 0 for f in fre)         
        