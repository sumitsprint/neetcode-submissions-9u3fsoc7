class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map1 = {}

        for n in nums:
            map1[n] = map1.get(n, 0) + 1

        
        buckets = [[] for _ in range(len(nums) + 1)]

        for key, value in map1.items():
            buckets[value].append(key)

        ans = []    

        for i in range(len(buckets)-1, -1 , -1):    
            for n in buckets[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans





        
        