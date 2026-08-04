class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        can1 = can2 = None
        c1= c2 = 0

        for n in nums:
            if n == can1:
                c1 += 1

            elif n == can2:
                c2 += 1


            elif c1 == 0:
                can1 = n
                c1 = 1

            elif c2 == 0:
                can2 = n
                c2=1

            else:
                c1 -= 1
                c2 -= 1

        c1 = c2 = 0
        res = []
        for n in nums:
            if n == can1:
                c1 += 1
            elif n == can2:
                c2 += 1

        if c1 > len(nums) // 3:
                res.append(can1)

        if c2 > len(nums) // 3:
                res.append(can2)
        return res            
                    
            
                            
        
                

                    
        