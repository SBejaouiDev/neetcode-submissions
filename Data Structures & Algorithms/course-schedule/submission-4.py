class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Kahn's algoirthm

        1)  - create adjacency list
            - Compute all indegress of all nodes
        2) initalize a queue for indegress of zero 
        3) while the q is not empty: 
            - remove a node from the queue
            - for each neighbor v of u, decrease its indegree. If a neighors indegree equals 0 append to queue
            - if total amount of nodes == visited there is no cycle 

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

        print(numCourses, visited)
        # If visited nodes == total classes no cycle exists
        # if visited Nodes != numCourses no cycle exists 
       
        # numCourses = total number of classes
        # visited = classes we were able to process
        """
        To detect a cycle the nodes processed should not equal total number of nodes(classes)
        If we cannot process all nodes then some nodes were stuck creating a cycle

        You couldn't process every course → cycle exists → you cannot finish.
        """

        return visited == numCourses




