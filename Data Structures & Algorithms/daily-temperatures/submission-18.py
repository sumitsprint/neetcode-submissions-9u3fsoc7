class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        n = len(temp)
        ans = [0] * n

        for i in range(n):
            while stack and temp[i] > temp[stack[-1]]:
                
                ans[stack[-1]] =  i - stack[-1]
                stack.pop()
            stack.append(i)
            
        return ans
        