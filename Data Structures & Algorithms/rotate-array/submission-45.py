class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def isp(l,r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            return nums    

        k = k % len(nums)

        isp(0, len(nums) - 1)
        isp(0, k-1)
        isp(k, len(nums) - 1)



