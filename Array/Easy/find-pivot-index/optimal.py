class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        left = 0
        total = 0
        for i in range(0,n):
            total+=nums[i]
        for i in range(0,n):
            right = total - nums[i]-left
            if left == right:
                return i
            else:
                left+=nums[i]
        return -1