class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = [ [] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # create adj and indegree list 
        for src,dist in prerequisites: 
            print(src,dist)
            indegree[dist] += 1 
            adj[src].append(dist)

        print(indegree)
        print(adj)

        # append nodes with indegree of 0 to a queue
        q = deque()

        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)

        visited = 0

        # run top sort bfs
        while q: 
            visited += 1
            node = q.popleft()

            ## for every neighboor v of u: 
            """ 
            For the current node u. Look at its neighbors v 
            Decrement the indegree for that niehgbor node. if a neighbors indegree == 0 append to the queue 
            """
            for nei in adj[node]: 
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

    
        # if visited == numCourses we do not have a cycle. The amount of visited nodes should equal the amount of courses. 
        print(visited, numCourses)
        return visited == numCourses


