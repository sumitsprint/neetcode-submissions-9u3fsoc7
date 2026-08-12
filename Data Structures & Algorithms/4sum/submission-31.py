class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                left = j+1
                right = len(nums) - 1
                

                while left < right:
                    t= nums[left] + nums[right] + nums[i] + nums[j]
                    if t > target:
                        right -= 1
                    elif t< target:
                        left += 1
                    else:
                        ans.append([nums[left], nums[right], nums[i], nums[j]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1] and nums[right] == nums[right + 1]:
                            left += 1
                            right -= 1
        return ans                            


                    

                     


        