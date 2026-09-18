class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        #find peak
        left = 0
        right = mountainArr.length() - 1

        while left < right:
            mid = (left + right) // 2

            if mountainArr.get(mid) < mountainArr.get(mid+1):
                left = mid + 1
            else:
                right = mid

        l = 0
        r = right

        while l <= r:
            mid = (l+r) // 2

            if mountainArr.get(mid) == target:
                return mid

            elif mountainArr.get(mid) > target:
                r = mid - 1

            else:
                l = mid + 1

        l1 = right
        r2 = mountainArr.length() - 1
        while l1 <= r2:
            mid = (l1+r2) // 2

            if mountainArr.get(mid) == target:
                return mid

            elif mountainArr.get(mid) > target:
                l1 = mid + 1

            else:
                r2 = mid - 1


        return -1                           




            



        