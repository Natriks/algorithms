import math


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.getNumber(l1)
        b = self.getNumber(l2)
        return self.getLinkedList(a + b)

    def getNumber(self, list_node: ListNode):
        num = 0
        multiplier = 1
        while list_node:
            num += list_node.val * multiplier
            multiplier *= 10
            list_node = list_node.next
        return num

    def getLinkedList(self, num: int):
        node = None
        temp = None
        while num > 0:
            if node:
                temp = node
            node = ListNode(val=num % 10)
            node.next = temp
            num = math.floor(num / 10)
        return node


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
result = sol.addTwoNumbers(a, a2)
print(result)
