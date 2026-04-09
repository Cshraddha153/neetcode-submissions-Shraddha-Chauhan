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
        old_to_new = {None:None}
        curr = head
        while curr:
            copy = Node(curr.val)
            old_to_new[curr] = copy
            curr = curr.next
        
        ele = head
        while ele:
            node = old_to_new[ele] 
            node.next = old_to_new[ele.next]
            node.random = old_to_new[ele.random]
            ele = ele.next

        return old_to_new[head]
        

















