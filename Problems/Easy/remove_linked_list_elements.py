# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'val={self.val}, next={self.next}'


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev, curr = None, head
        while curr and prev:
            if curr.val == val:
                prev.next = curr.next
            curr = curr.next
            prev = prev.next
        return head


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
sol = Solution()
result = sol.removeElements(a, 2)
print(0)
