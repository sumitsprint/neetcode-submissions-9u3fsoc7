class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        
        window = defaultdict(list)

        for s in strs:
            fre = [0] * 26
            
            for c in s:
                fre[ord(c)-ord('a')] += 1
            window[tuple(fre)].append(s)   
        return list(window.values())     


        