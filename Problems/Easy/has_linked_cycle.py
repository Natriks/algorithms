# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        tortoise = head
        rabbit = head
        while True:
            if tortoise.next:
                tortoise = tortoise.next
            else:
                return False
            if rabbit.next and rabbit.next.next:
                rabbit = rabbit.next.next
            else:
                return False
            if tortoise == rabbit:
                return True


sol = Solution()
a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(-4)
a.next = b
b.next = c
c.next = d
d.next = b
print(sol.hasCycle(a))

a = ListNode(1)
b = ListNode(2)
a.next = b
b.next = a
print(sol.hasCycle(a))
