class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

    # Pass 1: Calculate Prefix products
    # output[i] will contain the product of all elements to the left of i
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

    # Pass 2: Calculate Suffix products on the fly
    # Multiply the existing prefix product by the suffix product
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output
        