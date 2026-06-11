class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            for j in range(i+1,n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left = j+1
                right = n -1

                while left < right:
                    total = nums[left] + nums[right] + nums[i] + nums[j]

                    if total == target:
                        res.append([nums[left], nums[right], nums[i], nums[j]])
                        left += 1
                        right -= 1
                        while left < right and nums[left]== nums[left-1] and nums[right] == nums[right+1]:
                            left += 1
                            right -= 1
                    elif total > target:
                        right -= 1
                    else:
                        left += 1

        return res                               


        