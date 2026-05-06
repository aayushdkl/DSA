class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        write = 0
        for read in range(0,n):
            if nums[read]!=0:
                nums[write],nums[read]=nums[read],nums[write]
                write+=1
        return nums