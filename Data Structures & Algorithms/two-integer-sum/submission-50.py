class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        flyMap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in flyMap:
                return [flyMap[diff], i]
            flyMap[nums[i]] = i    
        