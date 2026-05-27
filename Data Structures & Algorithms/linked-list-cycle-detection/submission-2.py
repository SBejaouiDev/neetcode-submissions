# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        index = -1
        h = {}
        curr = head

        # while curr:
        #     if curr in h:
        #         index = -1
        #         return True
        #     index += 1
        #     h[curr] = index
        #     curr = curr.next

        # #set approach 
        # s = set()
        # while curr:
        #     if curr in s:
        #         return True
        #     s.add(curr)
        #     curr = curr.next

        #fast and slow method

        slow = head
        fast = head
        while fast and fast.next: 

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
    


        return False

            
            

            
            
