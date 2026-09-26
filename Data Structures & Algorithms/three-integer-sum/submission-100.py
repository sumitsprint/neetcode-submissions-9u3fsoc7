class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # target = 0
        ans = []

        for i in range(len(nums)):
            if i> 0 and nums[i] == nums[i-1]:
                continue 
            left = i+1
            right = len(nums) - 1

            while left < right:
                total = nums[left] + nums[right] + nums[i]

                if total == 0:
                    ans.append([nums[left], nums[right], nums[i]])
                    left += 1
                    right -= 1

                    while left < right  and nums[right] == nums[right+1] and nums[left]  == nums[left-1]:
                        right -= 1
                        left += 1    



                elif total > 0:
                    
                    right -= 1    

                else:
                    
                    left += 1
        return ans                    
                    


