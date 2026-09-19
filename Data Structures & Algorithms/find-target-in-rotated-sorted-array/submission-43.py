class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]: # what if the range has only one element
            #The left boundary itself is a valid possible position

            #in normal binary search we naver compare mid with left and right
            # if i dont put equal sign in nums[left] it will jump to right side where target is not there
                if nums[left] <= target  < nums[mid]:

                    right = mid - 1
                else:
                    left = mid + 1

            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1