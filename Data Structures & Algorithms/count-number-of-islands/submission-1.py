class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Given a 2d grid where 1 represents land and 0 represents water count and return then number of islands


        island is formed by connecting adjacent land horizontally or vertically and is surrounded by water. 

        Run a dfs on the grid. We scan layer by layer. 

        We iterate through the grid. When we encounter a 1 we run dfs on that position. 
        In the DFS algo we change that marked position to zero, so that on the next execution of dfs we dont repeat values we have already counted
        when counting an island
        """

        # up down left right
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows = len(grid)
        cols = len(grid[0])
        island = 0 

        def dfs(r,c): 

           q = deque()
           grid[r][c] = "0"
           q.append((r,c))

           while q:

                r,c = q.popleft()
                #print(f"Visited cell: ({r}, {c}) with value {grid[r][c]}")
        

                for dr, dc in directions: 
                    nr, nc = dr + r, dc + c
                    #Check if the next position is correct
                    if (nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == "0"):
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = "0"
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    print(r,c)
                    dfs(r,c)
                    island += 1

        return island