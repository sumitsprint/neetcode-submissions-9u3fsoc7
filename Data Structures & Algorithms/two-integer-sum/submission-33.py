class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        flyMap = {}
        for i, n in enumerate(nums):
            ele = target - n
            if ele in flyMap:
                return [flyMap[ele], i]
            flyMap[n] = i
        return    

        