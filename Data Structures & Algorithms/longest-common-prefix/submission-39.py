class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        small = strs[0]
        ans = ''
        for s in strs:
            if len(s) < len(small):
                small = s
        for i in range(len(small)):
            for s in strs:
                if s[i] != small[i]:
                    return ans
            ans = ans + s[i]
        return ans            

            

                        
        