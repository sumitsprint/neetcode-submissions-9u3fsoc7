class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        current_index = 0
        n = len(nums)
        left = 0
        right = n - 1
        while current_index <= right:
            if nums[current_index] == 0:
                nums[left], nums[current_index] = nums[current_index], nums[left]
                left += 1
                current_index += 1

            elif nums[current_index] == 1:
                    current_index += 1

            else:
                nums[current_index], nums[right] = nums[right], nums[current_index]
                right -= 1

               
                








        