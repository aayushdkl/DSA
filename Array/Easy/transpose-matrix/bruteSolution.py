class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [[0]*len(matrix) for i in range(0,len(matrix[0]))]

        for r in range(0,len(matrix)):
            for c in range(0,len(matrix[0])):
                res[c][r]=matrix[r][c]
        return res