class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fre = [0] * 26
        for i in s:
            fre[ord(i)-ord("a")] += 1
        for i in t:
            fre[ord(i)-ord("a")] -= 1
        return all(f==0 for f in fre)

        