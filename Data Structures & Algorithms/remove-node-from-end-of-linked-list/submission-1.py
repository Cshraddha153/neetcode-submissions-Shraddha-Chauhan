# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        while n>0 and right:
            right = right.next
            # print(right.val)
            n-=1
        
        while right:
            left = left.next
            # print("left.val", left.val)
            right = right.next
            # print("right.val", right.val)

        left.next = left.next.next  
        return dummy.next