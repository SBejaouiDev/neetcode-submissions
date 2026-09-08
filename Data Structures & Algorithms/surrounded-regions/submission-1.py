class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Given a m x n matrix board containing letters x and o capture regions that are surrounded. 

        Plan:

        locate the regions with an o. 


        Run BFS on regions that contain 0. 
            while the q is not empty
                
                for each neighboor we check if 


        """
        def bfs(q):
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
        q = deque()
        #down up right left
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        for r in range(rows):
            for c in range(cols):
                # if o and not a border locations
                if (r == 0 or c == 0 or r == rows - 1 or c == cols -1) and board[r][c] == "O":
                        q.append((r,c))
   
        bfs(q)
        #print(board)
        for r in range(rows):
            for c in range(cols):
                # if o and not a border locations
                if board[r][c] == "O":
                    board[r][c] = "X"

                if board[r][c] == "T":
                    board[r][c] = "O"


        #print("testing",board)
        