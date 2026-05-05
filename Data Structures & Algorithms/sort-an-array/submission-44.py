class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # --- Your logic starts here ---
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        # Recursively split and sort
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        # Merge the sorted halves
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Add remaining elements
        result.extend(left[i:])
        result.extend(right[j:])

        return result
        # --- Your logic ends here ---