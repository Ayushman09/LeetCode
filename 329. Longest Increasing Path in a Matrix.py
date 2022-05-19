def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        DIR = [0, 1, 0, -1, 0]
        m, n = len(matrix), len(matrix[0])
        
        @lru_cache(None)
        def dfs(r, c):
            ans = 1
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i+1]
                if nr < 0 or nr == m or nc < 0 or nc == n or matrix[nr][nc] <= matrix[r][c]: continue  
                ans = max(ans, dfs(nr, nc) + 1)
            return ans
        
        ans = 0
        for r in range(m):
            for c in range(n):
                ans = max(ans, dfs(r, c))
        return ans