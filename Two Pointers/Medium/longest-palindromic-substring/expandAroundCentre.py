class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        def expandAlgo(self, left, right,s):
            while left>=0 and right < len(s) and s[left] == s[right]:
                left-=1
                right+=1
            return right -left-1
        start = 0
        end=0
        for i in range(0,len(s)):
            len1 = expandAlgo(self, i,i,s)
            len2=expandAlgo(self,i,i+1,s)

            maxLen = max(len1,len2)

            if maxLen>end-start:
                start = i-(maxLen-1)//2
                end = i+ maxLen//2
        return s[start:end+1]