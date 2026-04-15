class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True 

        # T.C - O(n + n) = O(n)
        # S.C- O(1)
        # Since the dictionary size is capped by the number of 
        # possible unique characters ($k$) and not the 
        # length of the string ($n$), we say the space is $O(k)$
        