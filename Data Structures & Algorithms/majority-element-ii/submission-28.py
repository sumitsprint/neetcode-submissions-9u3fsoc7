class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = count2 = 0
        candidate1 = candidate2 = None

        for n in nums:
            if count1 == 0:
                candidate1 = n
            elif count2 == 0:
                candidate2 = n

            if n == candidate1:
                count1 += 1

            elif n == candidate2:
                count2 += 1

            else:
                count1 -= 1
                count2 -= 1
        
        count1 = count2 = 0

        ans = []
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1    
        if count1 > len(nums) // 3:
            ans.append(candidate1)
        if count2 > len(nums) // 3:
            ans.append(candidate2)  

        return ans          
             

        
                






        