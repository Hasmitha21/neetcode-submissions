class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        #dfs

        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        ROWS,COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r,c):
            if(r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0"):
                return
            
            grid[r][c] = "0"
            for dr,dc in directions:
                dfs(r + dr, c+ dc)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands +=1
        return islands

        # ## ---- bfs -----
        # if not grid:
        #     return 0
        
        # rows = len(grid)
        # cols = len(grid[0])

        # visit = set()
        # islands = 0

        # def bfs(r,c):
        #     q = collections.deque()
        #     visit.add((r,c))
        #     q.append((r,c))
        #     while q:
        #         row,col = q.popleft()
        #         directions = [[1,0],[-1,0],[0,1],[0,-1]]

        #         for dr,dc in directions:
        #             r, c = row + dr, col + dc
        #             if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visit):
        #                 q.append((r, c))
        #                 visit.add((r, c))

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1" and (r,c) not in visit:
        #             bfs(r,c)
        #             islands += 1
        # return islands

        
