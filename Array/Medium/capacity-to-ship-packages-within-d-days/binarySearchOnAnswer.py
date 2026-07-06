import math
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        ans = 0

        def isValid(capacity):
            totalDays = 1
            totalWeight = 0
            for weight in weights:
                if totalWeight + weight > capacity:
                    totalDays += 1
                    totalWeight =0
                totalWeight+=weight
            return totalDays <=days


        while low<=high:
            mid = low + (high -low)//2
            if isValid(mid):
                ans = mid
                high = mid -1
            else:
                low = mid+1
        return ans