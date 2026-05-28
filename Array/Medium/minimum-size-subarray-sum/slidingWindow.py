class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        i,j,sum = 0,0,0
        minLength = float('inf')
        while(j<n):
            sum+=nums[j]
            while(sum>=target):
                minLength = min(minLength,j-i+1)
                sum-=nums[i]
                i+=1
            j+=1
        if minLength == float('inf'):
            return 0
        return minLength