# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val>l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next

            curr = curr.next
        
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

        return dummy.next

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val <list2.val:
                tail.next = list1
                list1 = list1.next 
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2
            
        return dummy.next