class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # DFS
        # directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        ROWS = len(grid)
        COLS = len(grid[0])

        # visited  = set()

        islands = 0

        def dfs(r,c):
            if (r <0 or c<0 or r >= ROWS or c >= COLS or grid[r][c] == '0'):
                return
            
            # visited.add(grid[r][c])
            grid[r][c] = "0"
            # for dr, dc in directions:
            #     dfs(r + dr, c + dc)
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
        
        return islands