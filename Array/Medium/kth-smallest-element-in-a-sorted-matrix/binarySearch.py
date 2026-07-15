from bisect import bisect_right

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        low = matrix[0][0]
        high = matrix[n - 1][n - 1]

        while low <= high:
            mid = low + (high - low) // 2

            count = 0
            for row in matrix:
                count += bisect_right(row, mid)

            if count < k:
                low = mid + 1
            else:
                high = mid - 1

        return low