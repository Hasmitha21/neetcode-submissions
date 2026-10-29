class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS= len(grid)
        COLS= len(grid[0])

        islands = 0
        visited = set()

        # def bfs(r,c):
            


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and ((r,c)) not in visited:
                    # bfs(r,c)
                    q = collections.deque()
                    q.append((r,c))
                    visited.add((r,c))
                    islands +=1

                    directions = [[1,0],[-1,0],[0,1],[0,-1]]
                    while q:
                        row, col = q.popleft()
                        for dr, dc in directions:
                            nr = row + dr
                            nc = col + dc
                            if (nr <0 or nc<0 or nr >=ROWS or nc >=COLS or grid[nr][nc]=="0" or (nr,nc) in visited):
                                continue
                            q.append((nr,nc))
                            visited.add((nr,nc))
        return islands

        # DFS

        # ROWS = len(grid)
        # COLS = len(grid[0])
        # directions = [[1,0],[-1,0],[0,1],[0,-1]]
        # islands = 0
        # visited = set()

        # def dfs(r,c):

        #     if (r<0 or c<0 or r>= ROWS or c>=COLS or grid[r][c] == "0" or (r,c) in visited):
        #         return
        #     visited.add((r,c))
        #     for dr, dc in directions:
        #         nr = r + dr
        #         nc = c + dc
        #         dfs(nr , nc)

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == "1" and (r,c) not in visited:
        #             dfs(r,c)
        #             islands += 1
        # return islands