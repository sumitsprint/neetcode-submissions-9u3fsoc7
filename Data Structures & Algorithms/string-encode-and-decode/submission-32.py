class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for s in strs:
            code += str(len(s)) + "#" + s
        return code    


    def decode(self, s: str) -> List[str]:
        current_index = 0
        res = []
        while current_index < len(s):
            hash_index = current_index
        
            while s[hash_index] != "#":
                hash_index += 1
            length = int(s[current_index:hash_index])
            word_start = hash_index + 1
            word_end = hash_index + length
            word = s[word_start:word_end + 1]
            res.append(word)
            current_index = word_end + 1
        return res    





