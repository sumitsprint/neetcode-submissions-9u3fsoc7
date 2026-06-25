class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        x = len(nums)

        for i in range(x):
            y = nums[i]
            while(y>0 and y < x+1 and nums[y-1] != y  ):
                idx = y - 1
                y, nums[idx] = nums[idx], y

        for i in range(x):
            if nums[i] != i + 1:
                return i+1
        return x +1                

        