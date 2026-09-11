class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        """
        Given n nodes labeled 0 to n-1 and a list of undirected edges. Write a function to check whether these edges make up a 
        valid tree.

        What defines a tree? 
            - Undirected connected graph that contains no cycles

        Check for cycles in graph. Can use BFS OR DFS. 
    
        BFS apporach

        - if number of edges > n -1 return False
        - build an adj list for the graph 
        - Use a set to mark the visted nodes
        - run dfs from node 0
            if dfs finds a visited node return false cycle exists
            else append to the visited set and run dfs on each neighbor for the current node. 

        return true if no cycles and all nodes are visited 

        """
        print(len(edges))
        if len(edges) > n - 1:
            return False
            
        visited = set()

        adj = [[] for _ in range(n)]

        #adj list to see where nodes point 
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        
        print(adj)

        #[[1, 2, 3], [0, 4], [0], [0], [1]]

        def dfs(node, parent):
            #cycle detected 
            if node in visited:
                return False

            visited.add(node)
            for neigh in adj[node]:
                #skipping the parent
                if neigh == parent:
                    continue

                if not dfs(neigh,node):
                    return False
                    
            return True

        return dfs(0,-1) and len(visited) == n 
