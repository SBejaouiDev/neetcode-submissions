class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Plan 
        Running a bfs on every single cell would be way too slow. We push all border cells into two queues. 
        We work backwards instead of foward. Instead of asking can this cell reach the ocean, which cells can
        reach the ocean if water flowed uphill.

        We run BFS on bordering ocean cells. 
            - pass 1 start at the pacfic coast let uphil water flow inward. Everywhere it touches can reach the pacific.
            - pass 2 opposite


        Pacific queue: all cells that border the pacific
        atlantic queue: all cells that border the atlantic

        boolean grid to Keep track of visited cells for each ocean searately 
        
        Run bfs on both pacific and atlantic queues. 
            - while the q is not empty we pop coordinates and mark true in the ocean grid
            - for each neighbor we check if its within the grid, has not been visited, and most importantly if the 
              


        """
        rows = len(heights)
        cols = len(heights[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        pacificVisited = [[False] * cols for _ in range(rows)]
        atlVisited = [[False] * cols for _ in range(rows)]

        #pq = deque([(r, c)])
        #aq = deque()

        def dfs(sources, oceanGrid):
            q = deque(sources)
            
            while q: 
                r,c = q.popleft()

                oceanGrid[r][c] = True 

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
        
                    if(0 <= nr < rows and 0 <= nc < cols and not oceanGrid[nr][nc] and heights[nr][nc] >= heights[r][c]):
                        q.append((nr,nc))
    
                
        pacificSources = []
        atlanticSources = []

        # for c in range(cols): 
        #     pacificSources.append((0, c))
        #     atlanticSources.append((rows - 1, c))

        # for r in range(rows):
        #     pacificSources.append((r, 0))
        #     atlanticSources.append((r, cols - 1 ))

        for r in range(rows):
            for c in range(cols):
                    # pacific queue
                    if 0 <= r < 1 or 0 <= c < 1:
                        pacificSources.append((r,c))

                    # atlantic queue
                    if c == cols - 1 or r == rows - 1:
                        
                        atlanticSources.append((r,c))
                        
        dfs(atlanticSources,atlVisited)
        dfs(pacificSources,pacificVisited)
   
        res = []
        for r in range(rows):
            for c in range(cols):
                if pacificVisited[r][c] and atlVisited[r][c]:
                    res.append([r,c])

        return res




