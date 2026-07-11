"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        """
        - copying linkedlist into a new section of memory
            **  None of the pointers in the new list should point to nodes in the OG list ** 
            - iterate through linkedlist creating copies. Create a new node for each node
            - store mem location in a hashset for fast look up O(1)
            
        """



        curr = head
        memLoc = {None: None}
        #dummy = curr.random
        
        while curr: 
            
            copy = Node(curr.val)
            memLoc[curr] = copy ## {og Node: copied Node
            print(curr.val,curr, curr.random)
            curr = curr.next

        
        curr = head

        while curr:
            copy = memLoc[curr] ## look up the copied node by og node
            copy.next = memLoc[curr.next]  ## point the copies node to its next copy node
            copy.random = memLoc[curr.random] ## point the random copy to its next copy node

            curr = curr.next

        return memLoc[head]

        #print("\n",memLoc, "\n")



