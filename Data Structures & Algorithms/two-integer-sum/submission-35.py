class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = defaultdict(list)
        for i, n in enumerate(nums):
            map1[n].append(i)
        for i, n in enumerate(nums):
            ele = target - n

            if ele in map1:
                for j in map1[ele]:
                    if j != i:
                        return [i, j]
                        
   



        
        