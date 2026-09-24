class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        fre = {}
        for n in nums:
            fre[n] = fre.get(n, 0)+1
        ans = []    

        for key, value in fre.items():
            if value > len(nums) // 3:
                ans.append(key)
        return ans        



        