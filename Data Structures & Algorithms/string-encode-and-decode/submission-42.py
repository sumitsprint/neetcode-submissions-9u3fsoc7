class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        current_index = 0
        
        while current_index < len(s):
            hash_index = current_index
            while s[hash_index] != "#":
                hash_index += 1
            length = int(s[current_index:hash_index])  
            word_start = hash_index + 1
            word_end = word_start + length
            word = s[word_start:word_end]  
            result.append(word)
            current_index = word_end 
        return result     




