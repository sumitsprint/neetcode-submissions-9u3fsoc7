from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # zip_longest fills shorter words with the fillvalue, which we filter out
        return "".join(c1 + c2 for c1, c2 in zip_longest(word1, word2, fillvalue=""))