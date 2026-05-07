class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        write = 0
        for read in range(0,n):
            if nums[read]!=nums[write]:
                write+=1
                nums[write]=nums[read]
        return write+1