class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded    


    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j+= 1
            l = int(s[i:j])
            word = s[j+1:j+l+1]
            res.append(word)
            i = j+l+1  
        return res      
                
                
             






