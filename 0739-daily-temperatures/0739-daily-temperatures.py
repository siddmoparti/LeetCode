class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []
        
        for right in range(len(temperatures)):
            while stack and temperatures[right] > temperatures[stack[-1]]:
                left = stack.pop()
                output[left] = right - left
            
            stack.append(right)
            
        return output
