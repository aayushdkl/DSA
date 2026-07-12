class Solution:
    def minLights(self, lights: list[int]) -> int:
        n = len(lights)
        diff = [0] * (n + 1)
        
        for i, v in enumerate(lights):
            if v > 0:
                diff[max(0, i - v)] += 1
                diff[min(n - 1, i + v) + 1] -= 1
                
        covered = [False] * n
        curr = 0
        for i in range(n):
            curr += diff[i]
            if curr > 0:
                covered[i] = True
                
        ans = 0
        i = 0
        while i < n:
            if not covered[i]:
                ans += 1
                i += 3
            else:
                i += 1
                
        return ans