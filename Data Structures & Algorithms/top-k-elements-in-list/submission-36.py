class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = {}
        ans = []

        for n in nums:

            occ[n]= occ.get(n,0) +1

        fre = [[] for _ in range(len(nums) + 1) ]

        for key, value in occ.items():
            fre[value].append(key)

        for i in range(len(fre)-1,-1,-1):
            for j in fre[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans








        