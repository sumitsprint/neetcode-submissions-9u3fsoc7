class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map1 = defaultdict(list)
        for n in strs:
            fre = [0] * 26
            for c in n:
                fre[ord(c) - ord('a')] += 1
            map1[tuple(fre)].append(n)
        return list(map1.values())      
        