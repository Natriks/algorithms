# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        current = head
        summator = 0
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            value = a + b + summator
            summator = 1 if value >= 10 else 0
            value = value - 10 if value >= 10 else value
            current.next = ListNode(value)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current = current.next
        if summator > 0:
            current.next = ListNode(summator)
        return head.next


a = ListNode(2)
b = ListNode(4)
c = ListNode(3)
a.next = b
b.next = c
a2 = ListNode(5)
b2 = ListNode(6)
c2 = ListNode(4)
a2.next = b2
b2.next = c2

sol = Solution()
res = sol.addTwoNumbers(a, a2)
