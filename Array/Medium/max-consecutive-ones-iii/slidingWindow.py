class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        i,j=0,0
        maxCount = 0
        kCount = k
        for j in range(0,n):
            if nums[j]==0:
                kCount -=1
            while kCount<0:
                if nums[i]==0:
                    kCount+=1
                i+=1
            maxCount= max(maxCount,j-i+1)
        return maxCount