class Solution:
    def reverseVowels(self, s: str) -> str:
        n= len(s)
        strs = list(s)
        left, right = 0,n-1
        vowels = {'a','e','i','o','u','A','E','I','O','U'}  
        while(left<right):
            while left<right and strs[left] not in vowels:
                left+=1
            while left<right and strs[right] not in vowels:
                right-=1
            if left<right:
                strs[left],strs[right]=strs[right],strs[left]
                left+=1
                right-=1
        return "".join(strs)