# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        num, curr = 0, head
        while curr:
            num += 1
            curr = curr.next
        if num == n:
            return head.next
        i, curr = 0, head
        while curr:
            if i == num - n - 1:
                if n == 1:
                    curr.next = None
                else:
                    curr.next = curr.next.next
            i += 1
            curr = curr.next
        return head
        