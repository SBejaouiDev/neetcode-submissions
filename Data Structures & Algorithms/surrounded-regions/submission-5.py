class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Given a m x n matrix board containing letters x and o capture regions that are surrounded. 

        Plan:
        1) Start bfs from border 0 cells, Mark reachable O's with T. This will create regions that cannot be surronded by x. 
        2) left over O's flipped to zero and T's back to zero.
        3) Final grid will represent 

        """
        def bfs():
            q = deque()

            for r in range(rows):
                for c in range(cols):
                    # if o and not a border locations
                    if (r == 0 or r == rows - 1 or c == 0 or c == cols -1) and board[r][c] == "O":
                            q.append((r,c))
            #q = deque([(r,c)])

            while q: 
                r, c = q.popleft()
      
                if board[r][c] == "O":
                    board[r][c] = "T"

                for dr, dc in directions: 
                    nr = r + dr
                    nc = c + dc

                    if (0 <= nr < rows and 0 <= nc < cols) and board[nr][nc] == "O": 
                        board[r][c] = "T"
                        q.append((nr,nc))

                    
        
        rows = len(board)
        cols = len(board[0])
        
        #down up right left
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        bfs()

        #traverse the whole board
        for r in range(rows):
            for c in range(cols):
                
                if board[r][c] == "O":
                    board[r][c] = "X"

                if board[r][c] == "T":
                    board[r][c] = "O"
        