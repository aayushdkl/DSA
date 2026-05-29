class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        prefixSum=[0]*(n+1)
        prefixSum[0]=0
        suffixSum=[0]*(n+1)
        suffixSum[n]=0

        for i in range(1,n+1):
            prefixSum[i]=prefixSum[i-1]+nums[i-1]
        for i in range(n-1,-1,-1):
            suffixSum[i]=suffixSum[i+1]+nums[i]

        for i in range(0,n):
            if prefixSum[i]==suffixSum[i+1]:
                return i
        return -1