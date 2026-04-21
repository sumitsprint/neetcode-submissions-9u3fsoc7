

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using a defaultdict avoids KeyErrors when the key is first seen
        res = defaultdict(list)
        
        for s in strs:
            # Create a frequency map for 'a' through 'z'
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            # Lists cannot be keys because they are mutable. 
            # We convert to a tuple so it can be hashed.
            res[tuple(count)].append(s)
            
        # Wrap in list() to ensure the return type matches the signature exactly
        return list(res.values())