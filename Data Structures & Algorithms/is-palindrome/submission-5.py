class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        t = ""
        f = ""
        for i in range(len(s)-1,-1,-1):
            if s[i].isalnum():
                t = t + s[i].lower()

        
        for i in range(len(s)):

            if s[i].isalnum():

                f= f + s[i].lower() 
        if f == t:
            return True
        else:
            return False                 



            
        