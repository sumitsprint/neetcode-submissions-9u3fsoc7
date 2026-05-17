class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        flyMap = {}
        for i in range(len(nums)):
            n = nums[i]
            diff = target - n
            if diff in flyMap:
                return [flyMap[diff], i]
            flyMap[n] = i    
        
        