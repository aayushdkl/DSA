class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        low,high =0,n-1
        ans =n
        while(low<=high):  
            mid = low+(high-low)//2
            if nums[mid]>=target:
                high = mid-1
                ans = mid
            else:
                low = low+1
        return ans