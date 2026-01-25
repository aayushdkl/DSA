class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        hashMap = {}
        for i in range(0,n):
            hashMap[nums[i]]=hashMap.get(nums[i],0)+1

        for num,freq in hashMap.items():
            if freq > 1:
                return True
        return False