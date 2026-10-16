class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # ----- MULTI SOURCE BFS ------ #
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        q = collections.deque()

        def addCell(r,c):
            if(r<0 or c<0 or r>=ROWS or c>=COLS or (r,c) in visited or grid[r][c] == -1):
                return
            visited.add((r,c))
            q.append([r,c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))

        
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist

                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    addCell(r+dr, c+ dc)
            dist += 1



        

        # DFS ---- did not work
        # ROWS = len(grid)
        # COLS = len(grid[0])
        # visited = set()

        # def dfs(r,c):
        #     if ( r<0 or c<0 or r>= ROWS or c >= COLS or grid[r][c] == -1 or (r,c) in visited ):
        #         return float("inf")
        #     directions = [[1,0],[-1,0],[0,1],[0,-1]]

        #     if grid[r][c] == 0:
        #         return 0
            
        #     visited.add((r,c))
        #     res = float("inf")
        #     for dr, dc in directions:
        #         res = min(res, 1 + dfs(r+dr, c+dc))
        #     visited.remove((r,c))
        #     return res



        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == float("inf"):
        #             grid[r][c] = dfs(r,c) 