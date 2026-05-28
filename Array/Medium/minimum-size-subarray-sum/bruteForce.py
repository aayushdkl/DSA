class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        length = float('inf')
        for i in range(0,n):
            sum=0
            for j in range(i,n):
                    sum+=nums[j]
                    if sum>=target:
                        length = min(j-i+1,length)
                        break
        if length == float('inf'):
            return 0
        return length