class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0
        a = []

        while p1 < len(word1) and p2 < len(word2):
            a.append(word1[p1])
            a.append(word2[p2])
            p1+=1
            p2+=1

        a.extend(word1[p1:])
        a.extend(word2[p2:])    
        return "".join(a)    








        