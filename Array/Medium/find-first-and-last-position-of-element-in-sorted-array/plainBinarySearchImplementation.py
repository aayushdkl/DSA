class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n= len(nums)
        first = self.firstOccurence(nums,n,target)
        if first == -1:
            return [-1,-1]
        last = self.lastOccurence (nums,n,target)
        return [first,last]

    def firstOccurence(self, nums,n,target):
        low,high = 0,n-1
        ans = -1
        while(low<=high):
            mid = low + (high - low)//2
            if nums[mid]==target:
                ans = mid
                high = mid-1
            elif nums[mid]<target:
                low = mid+1
            else:
                high = mid-1
        return ans

    def lastOccurence(self, nums,n,target):
        low,high = 0,n-1
        ans = -1
        while(low<=high):
            mid = low + (high - low)//2
            if nums[mid]==target:
                ans = mid
                low = mid+1
            elif nums[mid]<target:
                low = mid+1
            else:
                high = mid-1
        return ans