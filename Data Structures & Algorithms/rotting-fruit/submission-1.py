class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        q = collections.deque()
        fresh = 0
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        

        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    if ( row+dr in range(ROWS) and col+dc in range(COLS)) and grid[row+dr][col+dc] == 1:
                        grid[row+dr][col+dc] = 2
                        q.append((row+dr,col+dc))
                        fresh -= 1
            
            time += 1
        
        return time if fresh == 0 else -1



