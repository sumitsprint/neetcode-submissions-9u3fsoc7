class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isp(l, r):
            left = l
            right = r
            while left < right:
                while left < right and not s[left].isalnum():
                    left += 1
                while left < right and not s[right].isalnum():
                    right -= 1
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                else:
                    return False
            return True 
        
        left = 0
        right = len(s) - 1
        count = 0
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return (isp(left + 1, right) or isp(left, right - 1))
            
        return True        
                
                       



                    


                    

            
        