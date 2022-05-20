def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] or obstacleGrid[~0][~0]: return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if m == 1 and n == 1: return 1
        d = {}

        def df(x, y):
            if (x, y) in d: return d[(x,y)]
            if x == m or y == n or obstacleGrid[x][y] == 1: return 0
            if x == m - 1 and y == n - 1: return 1
            d[(x,y)] = df(x, y + 1) + df(x + 1, y)
            return d[(x, y)]

        return df(0, 1) + df(1, 0)