class Solution:
    def sortColors(self, nums: List[int]) -> None:

        current = 0
        n = len(nums)
        right = n - 1
        low = 0

        while current <= right:
            if nums[current] == 0:
                nums[current], nums[low] = nums[low], nums[current]
                current += 1
                low += 1

            elif nums[current] == 1:
                current += 1

            else:
                nums[current], nums[right] = nums[right], nums[current]
                right -= 1
        return nums        





        
        