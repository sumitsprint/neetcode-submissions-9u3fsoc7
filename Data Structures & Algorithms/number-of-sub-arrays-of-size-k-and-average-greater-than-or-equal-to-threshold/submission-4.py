class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        dq = deque()
        ans = 0
        for i in range(len(arr)):
           

            dq.append(arr[i])

            if len(dq) > k:
                dq.popleft()


            if len(dq) == k:
                
                avg = sum(dq) / len(dq)
                if avg >= threshold:
                    ans += 1
        return ans



            


        






            



        