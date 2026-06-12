class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded    



    def decode(self, s: str) -> List[str]:
        
        ci = 0
        n = len(s)
        res = []
        while ci < n:
            hash_i = ci
            while s[hash_i] != "#":
                hash_i += 1
            length = int(s[ci:hash_i])
            word_start = hash_i + 1
            word_end = word_start + length
            word = s[word_start:word_end]
            res.append(word)
            ci = word_end
        return res    




