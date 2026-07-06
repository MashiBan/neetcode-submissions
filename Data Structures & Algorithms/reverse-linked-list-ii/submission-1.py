# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        leftprev = dummy
        for _ in range(left-1):
            leftprev = leftprev.next

        rightnode = leftprev.next
        for _ in range(right-left):
            rightnode = rightnode.next

        rightnext = rightnode.next
        rightnode.next = None

        newhead,newtail = self.reverse(leftprev.next)

        leftprev.next = newhead
        newtail.next = rightnext

        return dummy.next
    
    def reverse(self, head):
        dummy = head
        prev = None
        while dummy:
            nxt = dummy.next
            dummy.next = prev
            prev = dummy
            dummy = nxt
        return prev, head
