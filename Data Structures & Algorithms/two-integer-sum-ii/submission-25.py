class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            t = nums[left] + nums[right]
            if t > target:
                right -= 1
            elif t < target:
                left += 1
            else:
                return [left+1, right+1]        

            



        

        