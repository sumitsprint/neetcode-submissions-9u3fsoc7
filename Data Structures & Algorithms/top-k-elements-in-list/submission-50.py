class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = {}
        for n in nums:
            occ[n] = occ.get(n, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]    

        for key, value in occ.items():
            buckets[value].append(key)

        ans  = []    

        for i in range(len(buckets) - 1, -1, -1):
            for n in buckets[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans



            
    
        
        