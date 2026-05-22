class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)

        def reverseRow(row):
            left=0
            right = len(row)-1
            while left<=right:
                row[left],row[right]=row[right],row[left]
                left+=1
                right-=1
            
        for i in range(0,n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(0,n):
            reverseRow(matrix[i])
        
        # for i in range(0,n):
        #     matrix[i].reverse()