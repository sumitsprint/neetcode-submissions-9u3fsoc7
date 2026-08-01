class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" 
        for s in strs:
            res += str(len(s)) + "#" + s
        return res    
            

    def decode(self, s: str) -> List[str]:
        current = 0
        ans = []
        while current < len(s):
            hash_i = current
            while s[hash_i] != "#":
                hash_i += 1
            length = int(s[current:hash_i])
            word_s = hash_i + 1
            word_e = hash_i + length
            word = s[word_s:word_e+1]
            ans.append(word)
            current = word_e + 1
        return ans    



