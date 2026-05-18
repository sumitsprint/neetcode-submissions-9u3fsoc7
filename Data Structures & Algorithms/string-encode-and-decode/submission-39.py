class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for n in strs:
            encoded += str(len(n)) + "#" + n
        return encoded    


    def decode(self, s: str) -> List[str]:
        current_index = 0
        res = []
        while current_index < len(s):
            has = current_index
            while s[has] != "#":
                has += 1
            length = int(s[current_index:has])
            ws= has+1
            we = ws+length
            word = s[ws:we]
            res.append(word)
            current_index = we
        return res    





