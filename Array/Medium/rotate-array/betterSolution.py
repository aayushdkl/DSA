class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        temp=[0]*k
        for i in range(0,k):
            temp[i]=nums[n-k+i]
        for i in range(n-k-1,-1,-1):
            nums[i+k]=nums[i]
        for i in range(0,k):
            nums[i]=temp[i]
        return nums