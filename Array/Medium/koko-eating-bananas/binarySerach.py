from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(speed):
            hours = 0
            for pile in piles:
                hours += (pile + speed - 1) // speed
            return hours <= h

        low = 1
        high = max(piles)

        while low <= high:
            mid = low + (high - low) // 2

            if canFinish(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low