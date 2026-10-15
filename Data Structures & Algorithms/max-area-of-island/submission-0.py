class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        area = 0


        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            res = 1 # got 1 "1" so far
            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    new_r, new_c = dr + row, dc + col
                    if ( 0<= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c] != 0 and (new_r,new_c) not in visited):
                        q.append((new_r,new_c))
                        visited.add((new_r,new_c))
                        res += 1
            return res


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = max(area, bfs(r,c))
        
        return area
