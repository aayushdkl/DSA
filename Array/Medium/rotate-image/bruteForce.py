class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        ans = [[0]*n for i in range(0,n)]

        for i in range(0,n):
            for j in range(0,n):
                ans[j][n-1-i]=matrix[i][j]
        return ans