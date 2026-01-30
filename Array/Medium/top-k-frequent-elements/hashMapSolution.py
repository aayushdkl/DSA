class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)

        hashMap={}
        for val in nums:
            hashMap[val]=hashMap.get(val,0)+1
        sortedArray = sorted(hashMap.items(),key=lambda item: item[1],reverse=True)
        ans = []
        for i in range(k):
            ans.append(sortedArray[i][0])
        return ans