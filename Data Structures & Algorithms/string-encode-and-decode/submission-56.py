class Solution:

    def encode(self, strs: List[str]) -> str:
        result  = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result    

    def decode(self, s: str) -> List[str]:
        current = 0
        decoded = []
        while current < len(s):
            hash_ = current
            while s[hash_] != "#":
                hash_ += 1
            length = int(s[current:hash_])
            word_s = hash_ + 1
            word_e = word_s + length
            word = s[word_s:word_e]
            decoded.append(word)
            current = word_e
        return decoded       
