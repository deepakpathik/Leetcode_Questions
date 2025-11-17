from collections import deque

class Solution(object):
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])
        count = 0
        
        def bfs(i, j):
            q = deque([(i, j)])
            grid[i][j] = "0"
            while q:
                x, y = q.popleft()
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                        grid[nx][ny] = "0"
                        q.append((nx, ny))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    bfs(i, j)

        return count
