class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        sub = 0
        left = 0
        s = 0


        for right in range(n):
            s += arr[right]
            




            if right - left + 1 > k:
                s -= arr[left]
                left += 1
            if right - left + 1 == k:
                c = s / k
                if c >= threshold:
                    sub += 1    
        return sub





            


            



        