class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                index = stack[-1][1]
                res[index] += i - stack[-1][1]
                stack.pop()
            stack.append([temperatures[i], i])
        
        return res

        #[75,71,69,72,]
            
        