class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        hashMap = {}

        for num in nums:
            hashMap[num]=hashMap.get(num,0)+1
        buckets = [[] for i in range(0,n+1)]
        for val,freq in hashMap.items():
            buckets[freq].append(val)
        
        res = []
        for i in range(n,-1,-1):
            for val in buckets[i]:
                res.append(val)
            if len(res)==k:
                break
        return res