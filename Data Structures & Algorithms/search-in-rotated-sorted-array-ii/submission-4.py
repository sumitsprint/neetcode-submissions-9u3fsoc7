class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            # Case 1: Left half is sorted
            if nums[mid] > nums[right]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Case 2: Right half is sorted
            elif nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

            # Case 3: Duplicate detected (nums[mid] == nums[right])
            else:
                right -= 1

        return False