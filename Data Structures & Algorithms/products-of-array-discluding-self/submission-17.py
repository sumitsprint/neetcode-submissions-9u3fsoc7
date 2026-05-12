class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix = [1 for _ in range(len(nums))]
        prefix = []
        ans = [1] * len(nums)
        suffix = []
        f = 1
        fs = 1

        for i in range(len(nums)):
            f *= nums[i]
            prefix.append(f)

        for i in range(len(nums) - 1, -1, -1):
            fs *= nums[i]
            suffix.insert(0,fs)

        for i in range(len(ans)):
            if i == 0:
                ans[i] =  suffix [i + 1]
            elif i == len(ans) - 1:
                ans[i] = prefix[i - 1]   
            else:     

                ans[i] = prefix[i - 1] * suffix [i + 1]    
        return ans    


        