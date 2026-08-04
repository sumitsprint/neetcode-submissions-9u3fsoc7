class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        x= len(nums)
        for i in range(x):
            y = nums[i]
            while y > 0 and y <= x and y != nums[y - 1]:
                idx = y - 1
                nums[idx], y = y, nums[idx]

        for i in range(x):
            if nums[i] != i + 1:
                return i + 1
        return x + 1            

        