class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        total = m + n
        half = total // 2

        left = 0
        right = m

        while left <= right:

            # How many elements nums1 contributes to LEFT
            cut1 = (left + right) // 2

            # Remaining elements needed from nums2
            cut2 = half - cut1

            # Elements immediately around the cuts
            L1 = nums1[cut1 - 1] if cut1 > 0 else float("-inf")
            R1 = nums1[cut1] if cut1 < m else float("inf")

            L2 = nums2[cut2 - 1] if cut2 > 0 else float("-inf")
            R2 = nums2[cut2] if cut2 < n else float("inf")

            # Correct partition
            if L1 <= R2 and L2 <= R1:

                # Odd number of elements
                if total % 2:
                    return min(R1, R2)

                # Even number of elements
                return (max(L1, L2) + min(R1, R2)) / 2

            # Too many elements taken from nums1
            elif L1 > R2:
                right = cut1 - 1

            # Too few elements taken from nums1
            else:
                left = cut1 + 1
        

        
        