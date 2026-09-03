class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Given a matrix where 0 represents land and 1 represents water. Return the max area of an island in the grid. If no island exists return 0. 


        Plan: 
        Run a BFS and scan the grid layer by layer. 


        - Scan through the grid. When a one is encountered preform BFS. 
        - BFS will scan each layer. 
            - When a one is reached it will change that one to a zero, increment count, and then mvoe on to the next vertex.
            - When a 1 is not to be found execution of BFS will stop and return max count
            - Max of maxWeight and current max weight

        - The scanning of the grid for the next 1 will continue and the process above repeats until no 1's are to be found. 
        
        """

        #down up right left 
        directions = [ [1,0], [-1,0], [0,1], [0,-1] ]
        rows = len(grid)
        cols = len(grid[0])
        maxWeight = 0


        def bfs(r,c) -> int:
            q = deque()
            grid[r][c] = 0
            q.append((r,c))
            currWeight = 0

            while q:
                r, c = q.popleft()
                #print(f"\tVisited cell: ({r}, {c}) with value {grid[r][c]}")
                for dr,dc in directions:
                    nr, nc = dr + r, dc + c
                
                   # 
                    #nr = r + dr
                    #nc = c + dc
                    
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0:
                        #print("this executes")
                        
                        continue
                    currWeight += 1
                    q.append((nr,nc))
                    grid[nr][nc] = 0
                    #print("\tcurrWeight", currWeight)
                    
            return currWeight
            
        
        for r in range(rows): 
            for c in range(cols):
                if grid[r][c] == 1:
                    maxWeight = max(bfs(r,c) + 1,maxWeight)
                    print(maxWeight)
            
        return maxWeight
