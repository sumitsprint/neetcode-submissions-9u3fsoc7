class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1=count2 = 0
        ca= ca2 = None

        for n in nums:
            if n == ca:
                count1 += 1
            elif n == ca2:
                count2 += 1

            elif  count1 == 0:
                ca = n
                count1 =1
            elif count2 ==0 :
                ca2 = n
                count2 = 1

            else:
                count1 -=1
                count2 -= 1
        count1= count2 = 0   
        ans=[]     
        for n in nums:    
            if n == ca:
                count1 += 1
            elif n == ca2:
                count2 += 1
        if count1 > len(nums)//3:
            ans.append(ca)
        if count2 > len(nums)//3:
            ans.append(ca2)
        return ans                      


                
                        
                    
                


        