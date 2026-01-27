class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # n1 = len(s)
        # n2 = len(t)
        # hashMap = {}
        # for i in range(0,n1):
        #     hashMap[s[i]] = hashMap.get(s[i],0)+1
        # for i in range(0,n2):
        #     if t[i] in hashMap:
        #         if hashMap[t[i]]==0:
        #             return False
        #         else:
        #             hashMap[t[i]]=hashMap[t[i]]-1
        #     else :
        #         return False
        # for key in hashMap:
        #     if hashMap[key] != 0:
        #         return False
        # return True
        #Time Complexity: O(3n)
        #Space Complexity: O(n)

        #Just a bit of change:
        # n1 = len(s)
        # n2 = len(t)
        # if len(s)!=len(t):
        #     return False
        # hashMap = {}
        # for i in range(0,n1):
        #     hashMap[s[i]] = hashMap.get(s[i],0)+1
        # for i in range(0,n2):
        #     if t[i] in hashMap:
        #         if hashMap[t[i]]==0:
        #             return False
        #         else:
        #             hashMap[t[i]]=hashMap[t[i]]-1
        #     else :
        #         return False
        # return True
        #Time Complexity: O(2n)
        #Space Complexity: O(n)


        #Better way of dealing with characters:
        if len(s)!=len(t):
            return False
        hashMap = {}
        for ch in s:
            hashMap[ch] = hashMap.get(ch,0)+1
        for ch in t:
            if ch not in hashMap or ch ==0:
                return False
            else:
                hashMap[ch]-=1
        return True
        #Time Complexity: O(2n)
        #Space Complexity: O(n)