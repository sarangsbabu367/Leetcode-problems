from enum import Enum

class Direction(Enum):
    RIGHT = "right"
    LEFT = "left"
    TOP = "top"
    DOWN = "down"


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        visited = set()
        curr_num = 2
        i, j = 0, 0
        matrix = [[None]*n for _ in range(n)]
        matrix[0][0] = 1
        visited.add((0, 0))
        next_dir = Direction.RIGHT
        while True:
            if next_dir is Direction.RIGHT:
                j += 1
            elif next_dir is Direction.DOWN:
                i += 1
            elif next_dir is Direction.LEFT:
                j -= 1
            elif next_dir is Direction.TOP:
                i -= 1
            
            if j == n:
                j = n-1
                next_dir = Direction.DOWN
                continue
            if i == n:
                i = n-1
                next_dir = Direction.LEFT
                continue
            if j == -1:
                j = 0
                next_dir = Direction.TOP
                continue
            if i == -1:
                i = 0
                next_dir = Direction.RIGHT
                continue

            if (i, j) not in visited:
                visited.add((i, j))
                matrix[i][j] = curr_num
                curr_num += 1
            else:
                if next_dir == Direction.RIGHT:
                    j -= 1
                    next_dir = Direction.DOWN
                elif next_dir == Direction.DOWN:
                    i -= 1
                    next_dir = Direction.LEFT
                elif next_dir == Direction.LEFT:
                    j += 1
                    next_dir = Direction.TOP
                elif next_dir == Direction.TOP:
                    i += 1
                    next_dir = Direction.RIGHT
            
            if curr_num == (n**2)+1:
                break
        return matrix
        