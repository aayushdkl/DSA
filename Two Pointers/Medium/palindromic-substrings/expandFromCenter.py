class Solution:
    def countSubstrings(self, s: str) -> int:
        def countPalindrome(self,s, l,r):
            res=0
            while l>=0 and r<len(s) and  s[l]==s[r]:
                l-=1
                r+=1
                res+=1
            return res
        res = 0
        for i in range(0,len(s)):
            l=r=i
            res+= countPalindrome(self,s,l,r)
            l,r=i,i+1
            res+=countPalindrome(self,s,l,r)
        return res