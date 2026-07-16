class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def upperBound(arr,val):
            low = 0
            high = len(arr)-1
            while low<=high:
                mid = low + (high -low)//2
                if arr[mid]<=val:
                    low= mid+1
                else:
                    high = mid-1
            return low
        
        def count(matrix,val):
            c=0
            for row in matrix:
                c+=upperBound(row,val)
            return c
        n=len(matrix)
        low = matrix[0][0]
        high = matrix[n-1][n-1]
        while low<high:
            mid = low + (high - low)//2
            c=count(matrix,mid)
            if c<k:
                low = mid+1
            else:
                high = mid
        return low