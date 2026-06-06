class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        left = 0
        n = len(nums)
        right = n - 1
        k = k % n
        def rever(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            return nums

        rever(left, right)
        rever(left, k - 1)
        rever(k, right)        
        