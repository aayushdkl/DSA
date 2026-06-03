class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
         length = 0
         n=len(nums)
         hashMap = {}
         currSum = 0
         hashMap[0]=-1
         for i in range(0,n):
            if nums[i]==0:
                currSum-=1
            else:
                currSum+=1
            if currSum in hashMap:
                length = max(length,i-hashMap[currSum])
            else:
                hashMap[currSum]=i
         return length