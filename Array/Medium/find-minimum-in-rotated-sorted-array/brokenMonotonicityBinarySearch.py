class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        low,high = 0,n-1
        mini = float('inf')
        while low<=high:
            mid = low + (high - low)//2

            if nums[mid]>=nums[low]:
                mini = min(mini, nums[low])
                low = mid+1
            else:
                mini = min(mini, nums[mid])
                high = mid-1
        return mini