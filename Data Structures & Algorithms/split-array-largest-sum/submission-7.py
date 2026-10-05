class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        while left <= right:
            mid = (left + right) // 2

            cs= 0
            i = 0
            s =1

            while i < len(nums):
                if nums[i] + cs <= mid:
                    cs += nums[i]
                    i += 1

                else:
                    s += 1
                    cs = 0

            if s > k:
                left = mid + 1

            else:
                right = mid - 1

        return left        

                    
            


            