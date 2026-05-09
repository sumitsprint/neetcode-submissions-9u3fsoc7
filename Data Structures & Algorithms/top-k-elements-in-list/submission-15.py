class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = {}
        for n in nums:
            occ[n] = occ.get(n, 0) + 1

        fre = [[] for _ in range(len(nums)+1)]

        for key, value in occ.items():
            fre[value].append(key)
        res = []
        for i in range(len(fre)-1,-1,-1):
            for n in fre[i]:

                res.append(n)
                if len(res) == k:
                    
                    return res

        