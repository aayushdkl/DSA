class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if k<=1:
            return 0
        i=0
        prod = 1
        count = 0
        for j in range(0,n):
            prod*=nums[j]
            while prod>=k:
                prod//=nums[i]
                i+=1
            count+=(j-i+1)
        return count