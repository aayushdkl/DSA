class Solution:
    def countMonobit(self, n: int) -> int:
        count = 1 
        num = 1    

        while num <= n:
            count += 1
            num = (num << 1) | 1

        return count