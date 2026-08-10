class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1 = c2 =0
        can1 = can2 = None

        for n in nums:
            if n== can1:
                c1 += 1
            elif n == can2:
                c2 += 1
            elif c1 == 0:
                can1 = n
                c1 = 1    
            elif c2 == 0:
                can2= n
                c2 = 1   
            else:
                c1 -= 1
                c2 -= 1    

        c1 = c2 =0
        ans =[]
        for i in range(len(nums)):
            if nums[i] == can1:
                c1 += 1
            elif nums[i] == can2:
                c2 += 1

        if c1 > len(nums) // 3:
            ans.append(can1)  

        if c2 > len(nums) // 3:
            ans.append(can2)  
        return ans                  

        