class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        n= len(arr)

        num = 1
        for i in range(0,n):
            while not arr[i] == num:
                k-=1
                if k==0:
                    return num
                num+=1
            num+=1
        return arr[-1]+k