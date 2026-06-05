class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n= len(s)
        vowels = {'a','e','i','o','u'}
        count = 0
        for i in range(0,k):
            if s[i] in vowels:
                count+=1

        maxCount = count
        for i in range(k,n):
            if s[i] in vowels:
                count+=1
            if s[i-k] in vowels:
                count-=1
            maxCount = max(maxCount, count)
        return maxCount