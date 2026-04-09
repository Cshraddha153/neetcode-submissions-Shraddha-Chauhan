# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Reverse And Merge        
        # bring slow to mid
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # break into two ll
        # reverse second ll
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2





















        # #slow pointer in middle
        # slow, fast = head, head.next
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
            
        # # reverse second part
        # second = slow.next
        # prev = slow.next = None # first part separated
        # while second:
        #     temp = second.next  # temp=8, None
        #     second.next = prev  #  8->none  None->6
        #     prev = second  #prev=6   8
        #     second = temp  #second=8  None

        # #merge two ll
        # first, second = head, prev  # 2, 8
        # while second:
        #     temp1, temp2 = first.next, second.next  #4, 6
        #     first.next = second  # 8, 6
        #     second.next = temp1  #4, None
        #     first, second = temp1, temp2  # 4, 6


