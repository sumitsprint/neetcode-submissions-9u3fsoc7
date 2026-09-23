class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded    





    def decode(self, s: str) -> List[str]:
        h = 0
        c = 0
        ans = []
        while c < len(s):
            h = c
            while s[h] != "#":
                h += 1
            length = int(s[c:h])

            w = s[h+1:h+length+1]

            ans.append(w)
            c = h+length+1
        return ans    



        
