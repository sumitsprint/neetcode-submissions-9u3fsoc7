class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res    

    def decode(self, s: str) -> List[str]:
        result = []
        ci = 0
        while ci < len(s):
            hi = ci
            while s[hi] != "#":
                hi += 1
            length = int(s[ci:hi]) 
            w_s =  hi + 1
            w_e = w_s + length
            word = s[w_s:w_e]
            result.append(word)
            ci = w_e
        return result
              
                
                
            
