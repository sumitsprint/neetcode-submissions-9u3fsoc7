class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        flyMap = {}
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in flyMap:
                return [flyMap[diff], i + 1]
            flyMap[n] = i + 1   

        