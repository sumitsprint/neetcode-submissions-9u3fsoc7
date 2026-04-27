class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        flyMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff not in flyMap:
                flyMap[n] = i
            else:
                    
                return [flyMap[diff], i]    

        
        