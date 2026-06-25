class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded    




    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        while i < len(s):
            has = i
            while s[has] != "#":
                has += 1
            length = int(s[i:has])
            w_s = has + 1
            w_e = w_s + length
            word = s[w_s:w_e]
            ans.append(word)
            i = w_e


        return ans    






