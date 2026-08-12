class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
       
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums) - 1    

            while left < right:
                t =  nums[left] +  nums[right] + nums[i]

                if left < right and t > 0:
                    right -= 1
                elif left < right and t < 0:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right  and nums[left] == nums[left - 1] and nums[right] == nums[right+1]:
                        left +=1
                        right -= 1
        return ans            


                


            
