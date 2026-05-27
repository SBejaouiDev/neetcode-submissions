# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        index = -1
        count = 0 
        h = {}
        curr = head

        while curr:
            
            if curr in h:
                return True
            h[curr] = count
            curr = curr.next

        return False

            
            

            
            
