class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f = {}
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in f:
                return [f[diff], i+1]
            f[n] = i +1    
            