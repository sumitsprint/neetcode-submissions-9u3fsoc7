class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        f= {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in f:
                return [f[diff], i]
            f[n] = i    

        