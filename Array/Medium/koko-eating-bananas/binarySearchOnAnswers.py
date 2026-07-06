from typing import List
# import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = 0

        def isValid(speed):
            totalHours = 0
            for pile in piles:
                # totalHours += math.ceil(pile/speed)
                totalHours += (pile+speed-1)//speed
            return totalHours<=h

        while left<=right:
            mid = left + (right - left)//2
            if isValid(mid):
                ans = mid
                right = mid -1
            else:
                left = mid+1
        return ans