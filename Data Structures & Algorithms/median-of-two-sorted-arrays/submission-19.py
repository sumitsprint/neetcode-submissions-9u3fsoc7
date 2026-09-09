class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        total = n  + m
        half = total // 2

        left = 0
        right = m

        while left <= right:
            cut1 = (left + right) // 2
            cut2 = half - cut1

            l1 = nums1[cut1-1] if cut1 > 0 else float('-inf')
            r1 = nums1[cut1] if cut1 < m else float('inf')
            l2 = nums2[cut2-1] if cut2 > 0 else float('-inf')
            r2 = nums2[cut2] if cut2 < n else float('inf')

            if l1 <= r2 and l2 <= r1:
                if total % 2:
                    return min(r1,r2)
                return (max(l1,l2) + min(r1,r2)) / 2    
            if l1 > r2:
                right = cut1 - 1
            else:
                left = cut1 + 1        






        