# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes = set()
        while headA and headB:
            if headA == headB:
                return headA
            if headA in nodes:
                return headA
            if headB in nodes:
                return headB
            nodes.add(headA)
            nodes.add(headB)
            headA = headA.next
            headB = headB.next
        while headA:
            if headA in nodes:
                return headA
            headA = headA.next
        while headB:
            if headB in nodes:
                return headB
            headB = headB.next
        return None
