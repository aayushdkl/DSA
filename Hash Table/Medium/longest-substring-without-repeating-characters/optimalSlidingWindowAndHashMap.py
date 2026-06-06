class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        n=len(s)
        i,j=0,0
        hashMap={}
        while j<n:
            if s[j] in hashMap and hashMap[s[j]]>=i:
                i = hashMap[s[j]]+1
            hashMap[s[j]]=j
            maxLen = max(maxLen,j-i+1)
            j+=1
        return maxLen