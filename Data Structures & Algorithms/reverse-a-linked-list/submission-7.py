# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        node = head.next
        prev = head
        prev.next = None
        while node != None:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        return prev
