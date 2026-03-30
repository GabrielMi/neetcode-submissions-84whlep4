# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        prev, curr = None, head2
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head2, curr = prev, head
        while curr and head2:
            temp = curr.next
            temp2 = head2.next
            curr.next = head2
            head2.next = temp
            curr = temp
            head2 = temp2
