class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 2
        n = len(nums)
        for read in range(2,n):
            if nums[read]!=nums[write-2]:
                nums[write]=nums[read]
                write +=1
        return write