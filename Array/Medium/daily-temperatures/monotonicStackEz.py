class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n=len(temperatures)
        result = [0]*n
        stack = []

        for i in range(0,n):
            currentValue = temperatures[i]
            while stack and currentValue > temperatures[stack[-1]]:
                poppedIndex = stack.pop()
                result[poppedIndex] = i - poppedIndex
            stack.append(i)
        return result