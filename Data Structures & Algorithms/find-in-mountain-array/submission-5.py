class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        # 1. Find the peak index of the mountain array
        peak_left, peak_right = 0, n - 1

        while peak_left < peak_right:
            mid = (peak_left + peak_right) // 2

            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                peak_left = mid + 1
            else:
                peak_right = mid

        peak_index = peak_left

        # 2. Search in the strictly increasing part (left side up to peak)
        left, right = 0, peak_index

        while left <= right:
            mid = (left + right) // 2
            mid_val = mountainArr.get(mid)

            if mid_val == target:
                return mid
            elif mid_val > target:
                right = mid - 1
            else:
                left = mid + 1

        # 3. Search in the strictly decreasing part (peak to end)
        left, right = peak_index, n - 1

        while left <= right:
            mid = (left + right) // 2
            mid_val = mountainArr.get(mid)

            if mid_val == target:
                return mid
            elif mid_val > target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
                
                