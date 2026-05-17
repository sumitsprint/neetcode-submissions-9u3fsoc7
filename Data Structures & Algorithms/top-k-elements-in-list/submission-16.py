class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = {}
        res = []
        for i,n in enumerate(nums):
            occ[n] = occ.get(n, 0) + 1

        buckets = [[] for _ in range(len(nums)+1)]

        for key, value in occ.items():
            buckets[value].append(key)

        for i in range(len(buckets)-1,-1,-1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res            
             



        