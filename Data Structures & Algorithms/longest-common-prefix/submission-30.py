class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        small = strs[0]
        for s in strs:
            if len(s) < len(small):
                small = s
        ans = ""
        for i in range(len(small)):
            match_count = 0
            for s in strs:
                if small[i] == s[i]:
                    match_count += 1  
            if match_count == len(strs):
                ans += s[i]
            else:
                break

        return ans            


                            