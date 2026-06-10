class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1 = c2 = None
        co = co2 = 0
        ans = []

        for n in nums:
            if n == c1:
                co += 1
            elif n == c2:
                co2 += 1

            elif co == 0:
                c1 = n
                co = 1
            elif co2 ==0:
                c2 = n
                co2 += 1
            else:
                co -= 1
                co2-=1

        co=co2 =0
        for n in nums:
            if n == c1:
                co+=1
            elif n == c2:
                co2+= 1
        if co >   len(nums)//3:

            ans.append(c1)
        if co2 > len(nums)//3:
            ans.append(c2)
        return ans                  


        
        
                
            
                                

        