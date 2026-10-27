class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # ROWS = len(grid)
        # COLS = len(grid[0])

        # directions = [[1,0],[-1,0],[0,1], [0,-1]]
        # visited = set()
        # area = 0

        # def dfs(r,c):
        #     if (r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c]==0 or (r,c) in visited):
        #         return 0
            
        #     visited.add((r,c))
        #     curr_area = 1
        #     for dr,dc in directions:
        #         nr = r + dr
        #         nc = c + dc
        #         curr_area += dfs(nr,nc)
        #     return curr_area
            

        # for r in range(ROWS):
        #     for c in range(COLS):
        #             area = max(area, dfs(r,c))
        # return area

        # BFS
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [[1,0],[-1,0],[0,1], [0,-1]]
        visited = set()
        area = 0

        def bfs(r,c):

            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            curr_area = 1
            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if (nr <0 or nc <0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0 or (nr,nc) in visited):
                        continue
                    
                    q.append((nr,nc))
                    visited.add((nr,nc))
                    curr_area += 1
            return curr_area

                    


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, bfs(r,c))
        return area
