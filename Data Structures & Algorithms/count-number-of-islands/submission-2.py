class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # DFS

        # ROWS = len(grid)
        # COLS = len(grid[0])
        # islands = 0
        # def dfs(r,c):
        #     if (r <0 or c<0 or r >= ROWS or c >= COLS or grid[r][c] == '0'):
        #         return           
        #     grid[r][c] = "0"
        #     dfs(r+1, c)
        #     dfs(r-1, c)
        #     dfs(r, c+1)
        #     dfs(r, c-1)       
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == "1":
        #             dfs(r,c)
        #             islands += 1
        
        # return islands


        # BFS

        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        islands = 0

        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    new_r = row + dr
                    new_c = col + dc
                    if (0 <= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c] == "1" and (new_r, new_c) not in visited):
                        q.append((new_r, new_c))
                        visited.add((new_r,new_c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        
        return islands