# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = list3 = ListNode()
        #list3 = list1
        #print(list3.val)

        while list1 and list2:

            # if list1.val == list2.val:
            #     list3 = list1
            #     list1 = list1.next
            #     list3.next = list2
            #     list2 = list2.next


            if list1.val < list2.val: 
                list3.next = list1
                list1 = list1.next
            else:
                list3.next = list2 
                list2 = list2.next
            #assume that they are equal 
            list3 = list3.next

        list3.next = list1 or list2

        return dummy.next

              