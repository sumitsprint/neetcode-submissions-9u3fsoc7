class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        see = set(nums)
        max_c = 0

        for n in see:
            if n-1 in see:
                continue
            count = 1
            s = n + 1
            while s in see:
                
                count += 1 
                s+=1
            max_c = max(max_c,count)
        return max_c        




        