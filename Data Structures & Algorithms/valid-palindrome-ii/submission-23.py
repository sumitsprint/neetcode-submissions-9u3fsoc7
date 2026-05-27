class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isp(l,r):
            while l<r:
                while not s[l].isalnum():
                    l+=1
                while not s[r].isalnum():
                    r-=1
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                else:
                    return False
            return True        
                 
            

        l = 0
        r = len(s) - 1
        while l < r:
            while not s[l].isalnum():
                l += 1
            while not s[r].isalnum():
                r -= 1

            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return (isp(l+1,r) or isp(l,r-1))
        return True            




        