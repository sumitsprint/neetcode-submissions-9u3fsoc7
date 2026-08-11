class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isp(l,r):
            while l < r:
                while l < r and not s[left].isalnum():
                    l += 1

                while l < r and not s[right].isalnum():
                    r -= 1    
                
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        left = 0
        n = len(s)
        right = n - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return isp(left, right-1) or isp(left+1, right)


        return True        







                    















                


                    
                    
        