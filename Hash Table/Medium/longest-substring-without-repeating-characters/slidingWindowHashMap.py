class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = float('-inf')
        hashMap = {}
        n=len(s)
        i,j=0,0

        while j<n:
            if s[j] not in hashMap:
                maxLen = max(maxLen, j-i+1)
                hashMap[s[j]]=j
                j+=1
            else:
                del hashMap[s[i]]
                i+=1
        if maxLen == float('-inf'):
            return 0          
        return maxLen