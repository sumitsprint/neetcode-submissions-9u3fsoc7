class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]    
        return res

        # tc- O(n*m)
        # sc-O(m)
        # res can grow up to the length of the shortest string (let’s call that m).

# You don’t store all n strings again; you just iterate
#  over them. Iteration doesn’t
#   add extra memory beyond what’s already given in input.
######'''


'''vffrv
'''