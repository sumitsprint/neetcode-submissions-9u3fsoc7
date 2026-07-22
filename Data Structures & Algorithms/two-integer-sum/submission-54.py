class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        flymap = {

        }
        for i, n in enumerate(nums):
            diff = target - n
            if diff in flymap:

                return list((flymap[diff], i))

            flymap[n] = i

        