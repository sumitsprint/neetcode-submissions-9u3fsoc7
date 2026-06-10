class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        up = 0
        down = 0
        res= []

        while up < len(word1) and down < len(word2):
            res.append(word1[up])
            res.append(word2[down])
            up += 1
            down += 1

        res.extend(word1[up:])
        res.extend(word2[down:])  

        return "".join(res)  
            




        