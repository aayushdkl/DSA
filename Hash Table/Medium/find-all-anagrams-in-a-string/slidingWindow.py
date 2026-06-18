class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n1,n2=len(s),len(p)
        if n1<n2:
            return []
        freqS,freqP = [0]*26,[0]*26
        ans = []
        for i in range(0,n2):
            freqS[ord(s[i])-ord('a')]+=1
            freqP[ord(p[i])-ord('a')]+=1
        if freqS == freqP:
            ans.append(0)
        left = 0
        for right in range(n2,n1):
            freqS[ord(s[left])-ord('a')]-=1
            freqS[ord(s[right])-ord('a')]+=1
            left+=1
            if freqS == freqP:
                ans.append(left)
        return ans