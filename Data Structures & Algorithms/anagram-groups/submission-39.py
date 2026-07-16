class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        fre = defaultdict(list)
        for s in strs:
            fr = [0] * 26
            for c in s:
                fr[ord(c) - ord('a')] += 1
            fre[tuple(fr)].append(s)    


        return list(fre.values())

        