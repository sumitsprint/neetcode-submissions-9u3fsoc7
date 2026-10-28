class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n = len(nums1)
        m = len(nums2)

        left = 0
        right = n
        total = n + m
        half = total // 2
        

        while left <= right:
            cut1 = (left + right) // 2
            cut2 = half - cut1
            
            L1 = nums1[cut1 - 1] if cut1 > 0 else float('-inf')
            L2 = nums2[cut2 - 1] if cut2 > 0 else float('-inf')
            R1 = nums1[cut1] if cut1 < n else float('inf')
            R2 = nums2[cut2] if cut2 < m else float('inf')

            if L1 <= R2 and L2 <= R1:
                if total % 2:
                    return min(R1, R2)
                return ((max(L1, L2) + min(R1, R2)) / 2) 
            
            elif L1 > R2:
                right = cut1 - 1

            else:
                left = cut1 + 1

                   

            


            
             
        





        