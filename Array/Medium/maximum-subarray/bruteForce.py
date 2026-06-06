class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        sum=0
        maxSum=float('-inf')
        for i in range(0,n):
            sum = 0
            for j in range(i,n):
                sum+=nums[j]
                maxSum = max(sum,maxSum)
        return maxSum