class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        windowSum = 0
        maxSum= float('-inf')
        for i in range(0,k):
            windowSum+=nums[i]
        maxSum = windowSum
        for i in range(k,n):
            windowSum+=nums[i]-nums[i-k]
            maxSum = max(maxSum, windowSum)
        return maxSum/k