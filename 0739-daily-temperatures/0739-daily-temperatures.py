class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # temp: 73,74,75,71,69,72,76,73
        # stack: 
            
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            
            while stack and temperatures[i] > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            
            stack.append(i)
        return res
