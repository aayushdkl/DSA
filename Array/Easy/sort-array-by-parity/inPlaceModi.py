class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n= len(nums)
        write = 0
        for read in range(0,n):
            if nums[read]%2==0:
                nums[write],nums[read]=nums[read],nums[write]
                write+=1
        return nums