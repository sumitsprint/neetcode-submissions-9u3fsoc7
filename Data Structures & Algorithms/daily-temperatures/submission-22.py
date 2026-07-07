class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        stack = []
        ans = [0] * n

        for i in range(n):
            while stack and temp[i] > temp[stack[-1]]:

                idx = stack[-1]
                ans[idx] = i - idx
                stack.pop()

            stack.append(i)
        return ans

