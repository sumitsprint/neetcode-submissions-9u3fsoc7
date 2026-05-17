class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = defaultdict(list)
        for i in range(len(nums)):
            map1[nums[i]].append(i)

        for i in range(len(nums)):
            n = nums[i]
            diff = target - n
            if diff in map1:
                for j in map1[diff]:
                    if j != i:
                        return [i,j]

        