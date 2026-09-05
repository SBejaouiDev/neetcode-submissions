class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0

        rows = len(grid)
        cols = len(grid[0])

       
        # Count total number of fresh oranges and positions of all rotten oranges.
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: 
                    fresh += 1 # count of how many oranges there are. 

                if grid[r][c] == 2: 
                    q.append((r, c))## queue of where all the rotten oranges are

        time = 0 

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q: 
            print(fresh, time, q)
        
            
            for _ in range(len(q)):
                r,c = q.popleft()

                #neighbor = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
                
                # For each rotten orange check it's 4 neighbors
                for dr, dc in directions:
                    row = r + dr 
                    col = c + dc 

                    if 0 <= row < rows and 0 <= col < cols  and grid[row][col] == 1:
                        grid[row][col] = 2
                        fresh -= 1
                        q.append((row,col))
                
            time += 1

        if fresh == 0:
            return time
        else:
            return -1 


