from collections import Counter, defaultdict

class Solution:
    def maximumWidth(self, planks: list[int]) -> int:
        count = Counter(planks)
        W = defaultdict(int)
        
        for k, v in count.items():
            W[k] += v
            
        keys = list(count.keys())
        n = len(keys)
        
        for i in range(n):
            x = keys[i]
            W[x + x] += count[x] // 2
            for j in range(i + 1, n):
                y = keys[j]
                W[x + y] += min(count[x], count[y])
                
        return max(W.values())