class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map1 = {

        }

        for n in nums:
            map1[n] = map1.get(n, 0) + 1

        fre = [[] for i in range(len(nums) + 1)]    

        for key, value in map1.items():
            fre[value].append(key)

        ans = []    

        for i in range(len(fre)-1, -1, -1):
            for s in fre[i]:
                ans.append(s)
                if len(ans) == k:
                    return ans
        return ans            
                


            
            
            

        