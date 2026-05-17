class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map1 = defaultdict(list)

        for s in strs:
            fre = [0] *26
            for c in s:
                fre[ord(c) -ord('a')] += 1
            map1[tuple(fre)].append(s)
        return list(map1.values())        


        