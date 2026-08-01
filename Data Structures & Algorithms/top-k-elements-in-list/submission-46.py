class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = {}
        n = len(nums)
        for j in nums:
            occ[j] = occ.get(j, 0) + 1

        fre = [[] for _ in range(n + 1)]

        for key, value in occ.items():
            fre[value].append(key)

        res = []

        for i in range(n, -1, -1):
            for m in fre[i]:
                res.append(m)
                if len(res) == k:
                    return res
