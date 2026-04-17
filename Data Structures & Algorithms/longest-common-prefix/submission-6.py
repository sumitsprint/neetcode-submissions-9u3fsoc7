class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = min(strs, key = len)
        res = ""
        for i in range(len(smallest)):
            for s in strs:
                if smallest[i] != s[i]:
                    return res
            res = res + s[i]    
        return res
            

        