class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def encrypt(x: int) -> int:
            s = str(x)
            return int(max(s) * len(s))
            
        return sum(encrypt(x) for x in nums)