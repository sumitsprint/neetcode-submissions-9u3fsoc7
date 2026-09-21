class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        high, current, low = len(nums) - 1, 0, 0
        while current <= high:
            if nums[current] == 0:
                #known region
                nums[current], nums[low] = nums[low], nums[current]
                low += 1
                current += 1
            elif nums[current] == 1:
                current += 1
            else:
                #unknown region
                nums[current] , nums[high] = nums[high], nums[current]   
                high -= 1
        return nums     


        #low is never inside the unknown region current has already processed form low to current
        # therefore the element can either be one or 0 if low == current
        # 2s are always kept in unknown region
        # think in terms of known region and unknown region

                

        