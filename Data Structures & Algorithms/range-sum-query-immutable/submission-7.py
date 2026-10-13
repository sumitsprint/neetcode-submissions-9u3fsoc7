class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

        # self.total = 0
        


        

    def sumRange(self, left: int, right: int) -> int:
        total = 0
        for i in range(left, right+1):
            total += self.nums[i]
        return total
        # return self.s


        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)