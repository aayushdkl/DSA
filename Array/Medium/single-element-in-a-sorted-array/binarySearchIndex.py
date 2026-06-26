class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        low,high = 0,n-1

        while low<=high:
            mid = low + (high-low)//2
            if mid < n - 1 and nums[mid]==nums[mid+1]:
                if (mid+1) % 2==0:
                    high = mid-1
                else:
                    low=mid+1
            elif mid >0  and nums[mid]==nums[mid-1]:
                if (mid) % 2==0:
                    high = mid-1
                else:
                    low=mid+1
            else:
                return nums[mid]