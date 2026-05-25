class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """ 
        m=len(matrix)
        n=len(matrix[0])

        temp = [[matrix[i][j] for j in range(n)] for i in range(m)]

        for i in range(0,m):
            for j in range(0,n):
                if matrix[i][j]==0:
                    for k in range(0,n):
                        temp[i][k]=0
                    for k in range(0,m):
                        temp[k][j]=0
        for i in range(m):
            for j in range(n):
                matrix[i][j]=temp[i][j]
        return matrix