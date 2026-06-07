class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        hashMap = {}
        i,j=0,0 
        maxCount = 0

        for j in range(0,n):
            hashMap[fruits[j]]=hashMap.get(fruits[j],0)+1
            if len(hashMap)<=2:
                maxCount = max(maxCount,j-i+1)
            else:
                hashMap[fruits[i]]-=1
                if hashMap[fruits[i]]==0:
                    del hashMap[fruits[i]]
                i+=1
        return maxCount