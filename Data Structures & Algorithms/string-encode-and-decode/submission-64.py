class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs: 
            encoded +=  str(len(s))  + "#" + s 
        return encoded    



    def decode(self, s: str) -> List[str]:
        ans = []
        current_index = 0
        

        while current_index < len(s):

            hash_index = current_index
            while s[hash_index] != "#":
                hash_index += 1

            word_length = int(s[current_index:hash_index])
            word_start = hash_index + 1
            word_end = word_start + word_length 
            word = s[word_start:word_end]
            ans.append(word)
            current_index = word_end
        return ans    




