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
        for _ in range(left - 1):
            print("idk",_)
            prev = prev.next

        print("prev", prev.val)
        printNode = prev 
        while printNode: 
            print(printNode.val)
            printNode = printNode.next
        print("\n")


        sublist_head = prev.next
        sublist_tail = sublist_head
        for _ in range(right - left):
            sublist_tail = sublist_tail.next
        
        print("testing the subList")
        printNode = sublist_head 
        while printNode: 
            print(printNode.val)
            printNode = printNode.next
        print("sublist tail",sublist_tail.val)
        print("sublist head",sublist_head.val)

        print("\n")

        next_node = sublist_tail.next
        sublist_tail.next = None
        reverseSubList = self.reverseList(sublist_head) ##reverse the list 
        prev.next = reverseSubList # 0 3 2 1 
        print("subListhead", sublist_head.val)
        sublist_head.next = next_node
        
        return dummy.next

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
