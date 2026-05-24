class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for i in range(n)]
        top, down, left, right = 0, n - 1, 0, n - 1
        dir = 0
        num = 1
        
        while top <= down and left <= right:
            if dir == 0:
                for i in range(left, right + 1):
                    matrix[top][i] = num
                    num += 1
                top += 1
                
            elif dir == 1:
                for i in range(top, down + 1):
                    matrix[i][right] = num
                    num += 1
                right -= 1
                
            elif dir == 2:
                for i in range(right, left - 1, -1):
                    matrix[down][i] = num
                    num += 1
                down -= 1
                
            elif dir == 3:
                for i in range(down, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1
            dir = (dir + 1) % 4
            
        return matrix