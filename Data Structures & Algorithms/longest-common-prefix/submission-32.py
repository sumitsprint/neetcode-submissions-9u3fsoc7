class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        small = strs[0]
        for s in strs:
            if len(s) < len(small):
                small = s
        ans = ""
        for i in range(len(small)):
            for s in strs:
                if small[i] != s[i]:
                    return ans
            ans += s[i]
        return ans    
                            
        