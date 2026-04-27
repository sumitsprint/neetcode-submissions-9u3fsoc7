class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        small = strs[0]
        ans = ""
        for s in strs:
            if len(s) < len(small):
                small = s
            # small = min(len(small), len(s))
        
        for i in range(len(small)):
            match_count = 0
            for s in strs:

                if s[i] == small[i]:
                    match_count += 1
            if match_count == len(strs):
                ans= ans + s[i]
            else:
                break    

                        
                    
                
            
        return ans    
                        



        