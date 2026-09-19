class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        left = 0
        right = mountainArr.length() - 1

        while left < right:
            mid = (left + right) // 2

            if mountainArr.get(mid) < mountainArr.get(mid+ 1):
                left = mid + 1
            else:
                right = mid


        l = 0
        r = left

        while l <= r:
            mid = (l+r) // 2
            if mountainArr.get(mid) == target:
                return mid

            if mountainArr.get(mid) > target:
                r = mid - 1
            else:
                l= mid +1

        l = left
        r = mountainArr.length() - 1

        while l <= r:
            mid = (l+r) // 2
            if mountainArr.get(mid) == target:
                return mid

            if mountainArr.get(mid) > target:
                l = mid + 1
            else:
                r= mid -1
                
        return -1        









            

            
            
            
        
        