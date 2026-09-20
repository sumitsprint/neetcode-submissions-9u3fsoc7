class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        window_sum = sum(arr[:k])
        ans = 0

        if window_sum >= k * threshold:
            ans += 1

        for i in range(k, len(arr)):
            window_sum += arr[i]      # add incoming element
            window_sum -= arr[i - k]  # remove outgoing element

            if window_sum >= k * threshold:
                ans += 1

        return ans