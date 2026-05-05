class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n=len(s)
        strs = list(s)
        for i in range(0,n,2*k):
            strs[i:i+k]=reversed(strs[i:i+k])
        return "".join(strs)