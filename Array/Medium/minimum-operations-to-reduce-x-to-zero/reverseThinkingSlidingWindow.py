class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n= len(nums)
        totalSum = sum(nums)
        target = totalSum -x
        i=0
        currentSum = 0
        maxLen = -1
        if target == 0:
            return n
        if target < 0:
            return -1
        for j in range(n):
            currentSum +=nums[j]
            while currentSum > target and i<=j:
                currentSum-=nums[i]
                i+=1
            if currentSum == target:
                maxLen = max(maxLen, j-i+1)
            
        if maxLen == -1:
            return -1
        else:
            return n-maxLen