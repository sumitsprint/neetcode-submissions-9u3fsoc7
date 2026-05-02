class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # small = strs[0]
        ans = ''
        # for s in strs:
            # if len(s) < len(small):
                # small = s
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i] :
                    return ans
            ans = ans + s[i]
        return ans            

            

                        
        