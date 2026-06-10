class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1= count2 = 0
        cand1 = cand2 = None
        m = len(nums)
        for n in nums:
            

            

            if n == cand1:
                count1 += 1

            elif n == cand2:
                count2 += 1

            

            elif count1 == 0:
                cand1 = n 
                count1 = 1  
            elif count2 == 0:
                cand2 = n
                count2 = 1         

            else:
                count1 -= 1
                count2 -= 1 

        count1 = count2 = 0
        ans = []

        for n in nums:
            if n == cand1:
                count1 += 1
            elif n == cand2:
                count2 += 1

        if count1 > m//3:
            ans.append(cand1)
        if count2 > m//3:
            ans.append(cand2)
        return ans                
        
                




            
           
                               
        