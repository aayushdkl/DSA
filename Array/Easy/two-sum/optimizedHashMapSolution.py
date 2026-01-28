class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n= len(nums)
        hashMap = {}
        for i,num in enumerate(nums):
            more = target - nums[i]
            if more in hashMap:
                return [i,hashMap[more]]
            hashMap[num]=i