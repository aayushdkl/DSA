class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n=len(s)
        strs = list(s)
        for i in range(0,n,2*k):
            left = i
            pointToReverse = min(i+k-1,n-1)
            while left<pointToReverse:
                strs[left],strs[pointToReverse] = strs[pointToReverse],strs[left]
                left+=1
                pointToReverse-=1
        return "".join(strs)