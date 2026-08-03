# Pattern: Binary Search + Difference Array (Sweep Line)

class Solution:
    def minInitialStrength(self, monsters: list[int], boosts: list[list[int]]) -> int:
        n = len(monsters)
        diff = [0] * (n + 1)
        for l, r, v in boosts:
            diff[l] += v
            diff[r + 1] -= v
            
        bonus = [0] * n
        curr_b = 0
        for i in range(n):
            curr_b += diff[i]
            bonus[i] = curr_b
            
        def check(S):
            curr = S
            for i in range(n):
                if curr + bonus[i] < monsters[i]:
                    return False
                curr -= monsters[i]
                if curr < 0:
                    curr = 0
            return True
            
        left = 0
        right = sum(monsters)
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans