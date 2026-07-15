# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Find the leftBound val example l = 4 r = 6 listL: 1 2 3 4 5 6
        # prev would be 3. sublist head would be prev.next == 4
        for _ in range(left - 1):
            prev = prev.next

        # Find the right bound of the list example l = 4 r = 6 listL: 1 2 3 4 5 6
        # subList would be 4. right - left = 2. Iterate two times 5 -> 6
        # sublistTail = 6
        sublist_head = prev.next
        sublist_tail = sublist_head
        for _ in range(right - left):
            print(_)
            sublist_tail = sublist_tail.next
    
        
        next_node = sublist_tail.next # 1 2 3 - > 4 
        sublist_tail.next = None # 1 2 3 -> None
        reverseSubList = self.reverseList(sublist_head) ##reverse the list 123 = 321 
        prev.next = reverseSubList # 0 -> 3 2 1 
        sublist_head.next = next_node # 3 2 1 -> 4 -> 5

        return dummy.next # 3 2 1 4 5 

        printNode = prev 
        while printNode: 
            print(printNode.val)
            printNode = printNode.next
        



    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev 
            prev = curr
            curr = temp

        return prev
