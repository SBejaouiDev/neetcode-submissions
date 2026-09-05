class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:



        """ 
        Plan: 
        Run multi-source bfs. 
        Count the total amount of fresh oranges and the location of where the rotten fruit is. 

        While the queue is not empty and fresh > 0
            - we check it's 4 neighbors for fresh fruit. 
                - if fresh rot the fruit, decrement fresh, and append to q 
            - after a layer is processed increment time.

        if fresh count becomes 0 return time
        else return -1 representing that there is still fresh fruit
        """
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

            ## turns the problem into a mutliple source bfs problem.
            """ 
            With out this loop you would pop an orange, push rotten oranges and 
            increment the count for every single orange, breaking the timeline.

            so in the case where we have two rotten oranges. a mbfs should process all 3 in parallel during minute 1
            without the loop processing those 3 initial oranges would take 3 minutes.
            """
            for _ in range(len(q)):
                r,c = q.popleft()
                
                # For each rotten orange check it's 4 neighbors
                for dr, dc in directions:
                    row = r + dr 
                    col = c + dc 
                    
                    # if neighbor is fresh and within bounds, rotten, decrement fresh, and append to queue
                    if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                        grid[row][col] = 2
                        fresh -= 1
                        q.append((row,col))

            #after each bfs layer is processed increment time
            time += 1

        if fresh == 0:
            return time
        else:
            return -1 


