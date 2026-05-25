class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """ 
        m=len(matrix)
        n=len(matrix[0])

        isFirstRowZero= False
        isFirstColZero= False

        #Checking First Column
        for i in range(m):
            if matrix[i][0]==0:
                isFirstColZero=True

        #Checking First Row    
        for j in range(n):
            if matrix[0][j]==0:
                isFirstRowZero=True
        #Giving the resposibility to the first row and col , 
        #First row element rw first col element lai use grne track grna lai
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        
        #In-place modificatino
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        
        #corner case handle
        for i in range(0,m):
            if isFirstColZero:
                matrix[i][0]=0
        for j in range(0,n):
            if isFirstRowZero:
                matrix[0][j]=0