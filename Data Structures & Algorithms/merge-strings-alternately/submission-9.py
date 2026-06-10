class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = 0
        right = 0
        res = []  # Use a list instead of a string

        while left < len(word1) and right < len(word2):
            res.append(word1[left])
            res.append(word2[right])
            left += 1
            right += 1

        # Append the remaining slices
        res.append(word1[left:])
        res.append(word2[right:])
        
        return "".join(res)  # Convert list to string in O(N + M) time

        # tc= O(n+m)
        # sc= O(n+m)
        