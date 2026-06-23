class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        first = self.firstOccurrence(nums,n,target)
        if first == n:
            return [-1,-1]

        last = self.lastOccurrence(nums,n,target)
        return [first,last]

    def firstOccurrence(self,nums,n,target):
            ans = n
            low = 0
            high = n-1
            while(low<=high):
                mid = low + (high-low)//2
                if nums[mid]==target:
                    ans = mid
                    high = mid-1
                elif nums[mid]>target:
                    high = mid-1
                else:
                    low = mid+1
            return ans

    def lastOccurrence(self,nums,n,target):
            ans = n
            low = 0
            high = n-1
            while(low<=high):
                mid = low + (high-low)//2
                if nums[mid]==target:
                    ans = mid
                    low = mid+1
                elif nums[mid]<target:
                    low = mid+1
                else:
                    high = mid-1
            return ans