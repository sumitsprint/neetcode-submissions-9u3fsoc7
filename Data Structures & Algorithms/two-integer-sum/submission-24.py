class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = defaultdict(list)
        for i, n in enumerate(nums):
            map1[n].append(i)
        for i, n in enumerate(nums):
            diff = target - n
            if diff not in map1:
                continue
            for j in map1[diff]:
                if j != i:
                    return [i, j]


                
        