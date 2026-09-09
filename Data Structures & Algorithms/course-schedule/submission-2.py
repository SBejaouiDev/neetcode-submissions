class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """




        """
        adj = [ [] for _ in range(numCourses)]

        # Create adjacency list
        for edge in prerequisites:
            adj[ edge[0] ].append(edge[1])    

        # count of indegree 
        inDegree = [0] * numCourses

        #visitedNode count 
        visited = 0
        print(adj)

        # Compute in-degrees of all vertices
        for u in range(numCourses):
            for v in adj[u]:
                inDegree[v] += 1
                

        print(inDegree)

        q = deque()

        # Add all vertices with in-degree 0 to the queue
        for u in range(numCourses):
            if inDegree[u] == 0:
                q.append(u)
  
        #preform BFS top sort
        while q: 
            
            node = q.popleft()
            visited += 1

            for v in adj[node]:
                inDegree[v] -= 1

                if inDegree[v] == 0:
                    q.append(v)


         # If visited nodes != total nodes, a cycle exists

        #print(visited, v)
        # v = total number of nodes
        # visited = nodes we were able to process
        return visited == numCourses




