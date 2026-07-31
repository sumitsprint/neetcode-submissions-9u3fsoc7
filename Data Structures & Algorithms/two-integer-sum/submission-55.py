class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        fly = {}

        for i,n in enumerate(nums):
            diff = target - nums[i]
            
            if diff in fly:
                return [fly[diff], i]

            fly[n] = i
                

        