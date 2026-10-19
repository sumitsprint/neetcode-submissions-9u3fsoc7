class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        n = len(blocks)
        a = {}
        m = float('inf')

        for right in range(n):
            c = blocks[right]
            a[c] = a.get(c, 0) + 1

            while (right - left  + 1) > k:
                a[blocks[left]] -= 1
                left += 1

            if (right - left + 1) == k:
                m = min(m, a["W"] if "W" in a else 0)
        if m == float('inf'):
            return 0        
        return m        




        