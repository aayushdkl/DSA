class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        res = []
        m = len(matrix)
        n=len(matrix[0])

        top, down, left, right = 0, m-1,0,n-1
        dir = 0
        while top<=down and left<=right:
            if dir == 0:
                for i in range(left,right+1):
                    res.append(matrix[top][i])
                top+=1
            elif dir==1:
                for i in range(top,down+1):
                    res.append(matrix[i][right])
                right-=1
            elif dir==2:
                for i in range(right,left-1,-1):
                    res.append(matrix[down][i])
                down-=1
            elif dir==3:
                for i in range(down,top-1,-1):
                    res.append(matrix[i][left])
                left+=1
            dir+=1
            if dir==4:
                dir=0
        return res