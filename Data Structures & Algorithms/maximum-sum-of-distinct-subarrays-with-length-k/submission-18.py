class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n < k:
            return 0

        m_s = 0
        c_s = 0
        see = set()
        left = 0

        for i in range(n):
            # 1. Shrink from the left until the duplicate nums[i] is removed
            while nums[i] in see:
                see.remove(nums[left])
                c_s -= nums[left]
                left += 1

            # 2. Add current element
            see.add(nums[i])
            c_s += nums[i]

            # 3. Maintain window length of at most k
            if (i - left + 1) > k:
                see.remove(nums[left])
                c_s -= nums[left]
                left += 1

            # 4. Check if the window is valid and has size k
            if (i - left + 1) == k:
                m_s = max(m_s, c_s)

        return m_s