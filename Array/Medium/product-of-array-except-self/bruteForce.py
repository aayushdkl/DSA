class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prod = 1
        answer=[]
        for i in range(0,n):
            prod = 1
            for j in range(0,n):
                if i!=j:
                    prod*=nums[j]
            answer.append(prod)
        return answer