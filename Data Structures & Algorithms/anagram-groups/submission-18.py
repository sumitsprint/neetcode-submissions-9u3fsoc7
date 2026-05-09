class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:
            fre = [0] * 26
            for c in s:

                fre[ord(c) - ord('a')] += 1
            res[tuple(fre)].append(s)
        return list(res.values())        
        
        