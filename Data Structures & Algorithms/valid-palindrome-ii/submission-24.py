class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        l = 0
        r = n - 1
        def isp(l,r):
            while l < r:
                while l < r and not s[l].isalnum():
                    l+=1
                while l< r and not s[r].isalnum():
                    r-=1
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                else:
                    return False
            return True                    
        
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return isp(l, r-1) or isp(l+1, r)    
        return True        

                       