class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        low, high = 0, len(arr) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            missing_count = arr[mid] - (mid + 1)
            
            if missing_count < k:
                low = mid + 1
            else:
                high = mid - 1
        return low + k