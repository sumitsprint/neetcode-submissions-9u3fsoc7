class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        x = len(nums)
        for i in range(x):
            v = nums[i]
            while(v > 0 and v <= x and v != nums[v - 1]):
                idx = v - 1
                v, nums[idx] = nums[idx], v

        for i in range(x):
            if nums[i] != i + 1:
                return i +1
        return x + 1         

        