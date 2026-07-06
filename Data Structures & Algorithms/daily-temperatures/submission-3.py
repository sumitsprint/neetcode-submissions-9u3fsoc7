class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        n = len(temp)
        res = [0] * n

        for i in range(n):
            while stack and temp[i] > temp[stack[-1]]:
                idx = stack[-1] 
                res[idx] = i - stack[-1]
                stack.pop()

            stack.append(i)
        return res        
        
        