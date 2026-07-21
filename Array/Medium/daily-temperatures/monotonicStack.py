class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []       

        for i in range(n):
            current_temp = temperatures[i]
            while stack and current_temp > temperatures[stack[-1]]:
                popped_index = stack.pop()
                result[popped_index] = i - popped_index
            
            stack.append(i)

        return result