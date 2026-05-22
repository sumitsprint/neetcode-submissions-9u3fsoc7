class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = count2 = 0
        c1 = c2 = None

        for n in nums:
            if n == c1:
                count1 += 1
            elif n == c2:
                count2 += 1
            elif count1 == 0:
                c1 = n
                count1 = 1
            elif count2 == 0:
                c2 = n
                count2 = 1
            else:
                count1 -=1
                count2-= 1    

        ans = []
        count1 = count2 = 0
        for n in nums:
            if n == c1:
                count1+=1
            if n == c2:
                count2 += 1
        if count1 > len(nums)//3:
            ans.append(c1)
        if count2 > len(nums)//3:
            ans.append(c2)
        return ans                    


        