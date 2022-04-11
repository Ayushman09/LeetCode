def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        r, c = len(grid), len(grid[0])
        rst = [[None] * c for _ in range(r)]
        for i in range(r): 
            for j in range(c):
                ind = i * c + j + k
                rst[ind//c%r][ind%c] = grid[i][j]
        return rst