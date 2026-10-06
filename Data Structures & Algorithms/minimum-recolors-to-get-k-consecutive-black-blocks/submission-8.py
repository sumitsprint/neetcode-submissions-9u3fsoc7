class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)

        left = 0
        d = {}
        max_f = float("inf")

        for right in range(n):
            c = blocks[right]

            d[c] = d.get(c, 0) + 1
            

            length = right - left + 1

            

            if length > k:
                d[blocks[left]] -= 1
                
                
                left += 1
                length = right - left + 1

            if length == k:

                max_f = min(d.get("W", 0), max_f)
        return max_f        

#0 colud be the answer



        

            




            


        