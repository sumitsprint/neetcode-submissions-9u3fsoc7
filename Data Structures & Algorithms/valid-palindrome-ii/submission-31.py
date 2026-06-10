class Solution:
    def validPalindrome(self, s: str) -> bool:
        le = 0
        ri = len(s) - 1 
        def isp(l, r):
            while l < r:
                while l < r and not s[l].isalnum():
                    l += 1
                while l < r and not s[r].isalnum():
                    r -= 1

                if s[l].lower() == s[r].lower():
                    l+=1
                    r-= 1
                else:
                    return False
            return True

        while le < ri:
            while le < ri and not s[le].isalnum():
                le += 1
            while le < ri and not s[ri].isalnum():
                ri -= 1
            if s[le].lower() == s[ri].lower():
                le += 1
                ri -= 1
            else:
                return isp(le+1,ri) or isp(le, ri-1)     
        return True       









        