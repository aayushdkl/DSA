class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res =  [[] for i in range(len(nums))]
        left = 0
        right = n-1
        index = n-1
        while(left<=right):
            if abs(nums[left])>=abs(nums[right]):
                leftSquared = nums[left]*nums[left]
                res[index]=leftSquared
                index-=1
                left+=1
            else:
                rightSquared = nums[right]*nums[right]
                res[index]=rightSquared    
                index-=1
                right-=1
        return res