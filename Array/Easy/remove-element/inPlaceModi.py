class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        write=0
        k=0
        for read in range(0,n):
            if nums[read]!=val:
                # nums[read],nums[write]=nums[write],nums[read]
                #Doing this will place all the val elements at the end like move zeroes problem
                nums[write] = nums[read]
                #Since the values that are replaced doesnt matter, not matter if we dont put them in the array itself
                write+=1
                k+=1
        return k