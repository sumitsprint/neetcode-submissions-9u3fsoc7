class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for n in strs:
            code += str(len(n)) + "#" + n
        return code    


    def decode(self, s: str) -> List[str]:
        current_index = 0
        res = []
        while current_index < len(s):
            hash_index = current_index
            while s[hash_index] != "#":
                hash_index += 1
            length = int(s[current_index:hash_index])
            word = s[hash_index + 1:hash_index+1+length]
            res.append(word)
            current_index = length + 1 + hash_index
        return res    



