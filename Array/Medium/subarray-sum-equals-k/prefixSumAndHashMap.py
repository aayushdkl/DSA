class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixSum = [0]*n
        prefixSum[0]=nums[0]
        hashMap = {}
        ans = 0

        for i in range(1,n):
            prefixSum[i]=prefixSum[i-1]+nums[i]
        for r in range(0,n):
            if prefixSum[r]==k:
                ans+=1
            val = prefixSum[r]-k
            if val in hashMap:
                ans+=hashMap[val]
            hashMap[prefixSum[r]]=hashMap.get(prefixSum[r],0)+1
        return ans