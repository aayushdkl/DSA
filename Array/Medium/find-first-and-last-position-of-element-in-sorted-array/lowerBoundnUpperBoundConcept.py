class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n= len(nums)
        first = self.lowerBound(nums,n,target)
        if first == n or nums[first] != target:
            return [-1,-1]
        last = self.upperBound(nums,n,target)
        return [first,last-1]

    def lowerBound(self, nums,n,target):
        low, high= 0,n-1
        ans = n
        while(low<=high):
            mid = low + (high - low)//2
            if nums[mid] >= target:
                ans = mid
                high = mid -1
            else:
                low  = mid+1
        return ans

    def upperBound(self, nums,n,target):
        low, high= 0,n-1
        ans = n
        while(low<=high):
            mid = low + (high - low)//2
            if nums[mid] > target:
                ans = mid
                high = mid -1
            else:
                low  = mid+1
        return ans