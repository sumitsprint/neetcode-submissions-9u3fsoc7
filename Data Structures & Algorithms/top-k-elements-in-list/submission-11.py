class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = {}
        for n in nums:
            occ[n] = occ.get(n, 0) + 1

        buckets = [[] for _ in range(len(nums)+1)]
        for key, value in occ.items():
            buckets[value].append(key)
        res = []
        for i in range(len(buckets)-1,-1,-1):
            for num in buckets[i]:

                res.append(num)
                if len(res) == k:
                    return res


        