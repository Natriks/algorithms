# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        seen = set()
        node = head
        while True:
            if node in seen:
                return node
            else:
                seen.add(node)
            if node.next:
                node = node.next
            else:
                return None


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
