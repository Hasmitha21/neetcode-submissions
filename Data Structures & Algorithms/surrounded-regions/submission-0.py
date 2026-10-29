class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def capture():
            q = deque()
            for r in range(ROWS):
                for c in range(COLS):
                    if (r==0 or c==0 or r == ROWS-1 or c == COLS-1) and board[r][c] == "O":
                        q.append((r,c))
            
            while q:
                r,c  = q.popleft()
                if board[r][c] == "O":
                    board[r][c] = "T"
                    for dr, dc in directions:
                        nr = dr +r
                        nc = dc + c
                        if nr <0 or nc <0 or nr >= ROWS or nc >= COLS:
                            continue
                        q.append((nr,nc))
        
        capture()

        

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] ="X"
                elif board[r][c] == "T":
                    board[r][c] = "O"