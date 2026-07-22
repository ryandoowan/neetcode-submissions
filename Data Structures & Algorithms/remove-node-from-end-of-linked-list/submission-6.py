# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1 and head.next == None:
            return None
        
        node = head
        dummy = ListNode()
        dummy.next = head
        i = 1
        while node.next != None:
            if i >= n:
                dummy = dummy.next
            node = node.next
            i += 1
        
        if dummy.next == head:
            return head.next
        
        dummy.next = dummy.next.next
        return head
