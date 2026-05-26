class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        res = []

        # directions:
        # 0 -> right
        # 1 -> down
        # 2 -> left
        # 3 -> up
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]

        steps = 1
        dir = 0

        res.append([rStart, cStart])

        while len(res) < rows * cols:

            # same step count repeats twice
            for _ in range(2):

                dr, dc = dirs[dir]

                for _ in range(steps):

                    rStart += dr
                    cStart += dc

                    # only add if inside grid
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        res.append([rStart, cStart])

                dir += 1

                if dir == 4:
                    dir = 0

            steps += 1

        return res