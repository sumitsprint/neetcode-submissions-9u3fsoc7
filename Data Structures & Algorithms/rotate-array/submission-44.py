class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def rev(l,r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            return nums

        k = k % len(nums)

        rev(0,len(nums)-1)
        rev(0, k-1)
        rev(k, len(nums)-1)



        
        
        