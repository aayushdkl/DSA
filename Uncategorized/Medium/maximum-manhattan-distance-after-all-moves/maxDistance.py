class Solution:
    def maxDistance(self, moves: str) -> int:
        x = y = 0
        wild = 0

        for move in moves:
            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'R':
                x += 1
            elif move == 'L':
                x -= 1
            else:
                wild += 1

        return abs(x) + abs(y) + wild