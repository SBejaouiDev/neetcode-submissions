# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        dummy = l1

        curr = l1
        currTwo = l2
        
        head = None


        carry = 0
        sumed = 0
        while curr or currTwo: 
            #print(curr.val, currTwo.val)

            """
            99 
            99
            
            18 - 10 = 8
            """

            if curr and currTwo:
                sumed = curr.val + currTwo.val

            elif(curr and not currTwo):
                sumed = curr.val + 0

            elif(not curr and currTwo):
                 sumed = currTwo.val + 0
            
            if carry:
                sumed += 1
            if sumed > 10 or sumed == 10:
                carry = 1
                sumed = sumed - 10
            else: 
                carry = 0 
            head = self.add(head,sumed)
           


            if curr and currTwo:
                curr = curr.next
                currTwo = currTwo.next
            elif not curr and currTwo:
                currTwo = currTwo.next
            elif curr and not currTwo:
                curr = curr.next
        
          



        
        if carry:
            head = self.add(head,carry)

        self.print_linked_list(head)
        
        return head



    def add(self,head,value):

        new_node = ListNode(value)

        if head is None:
            return new_node

        curr = head

        while curr.next is not None:
            curr = curr.next
        
        curr.next = new_node

        return head


    def print_linked_list(self,head):
        current = head
        while current:
            print(current.val, end=" -> " if current.next else "\n")
            current = current.next