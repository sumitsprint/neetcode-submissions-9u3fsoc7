class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        left = 0
        right = 0
        ans = []

        while left < n and right < m:
            ans.append(word1[left])
            ans.append(word2[right])
            left += 1
            right += 1

        
        ans.append(word1[left:])

        
        ans.append(word2[right:])

        return "".join(ans)    

            



        