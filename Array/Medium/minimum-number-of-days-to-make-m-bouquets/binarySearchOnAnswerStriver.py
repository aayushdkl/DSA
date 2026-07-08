class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n=len(bloomDay)
        if m*k>n:
            return -1
        low,high = min(bloomDay),max(bloomDay)
        ans = -1
        def isPossible(bloomDay, day, m,k):
            cnt = 0
            noOfBouquet = 0

            for i in range (0,n):
                if bloomDay[i]<=day:
                    cnt+=1
                else:
                    noOfBouquet += (cnt//k)
                    cnt=0
            noOfBouquet += (cnt//k)
            if noOfBouquet < m:
                return False
            else:
                return True

        while low <=high:
            mid=low + (high-low)//2
            if isPossible(bloomDay,mid,m,k):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans