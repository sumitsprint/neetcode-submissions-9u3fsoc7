class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded    

    def decode(self, s: str) -> List[str]:
        res = []
        ci = 0
        while ci < len(s):
            hash_ = ci
            while s[hash_] != "#":
                hash_ += 1
            length = int(s[ci:hash_])
            w_s = hash_ + 1
            w_e = hash_ + 1 + length
            word = s[w_s:w_e]
            res.append(word)
            ci = w_e
        return res        


