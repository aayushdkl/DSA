class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        res = []
        
        for num in nums:
            if len(res) < k or num != res[-k]:
                res.append(num)
                
        return res