# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     if (not l1 and not l2) or (l1.val and not l2.val):
    #         return []

    #     result = []

    #     while l1 or l2:
    #         if not l1 and l2:
    #             result.append(l2.val)
    #             l2 = l2.next
    #         elif l1 and not l2:
    #             result.append(l1.val)
    #             l1 = l1.next
    #         elif l1.val < l2.val:
    #             result.append(l1.val)
    #             l1 = l1.next
    #         else:
    #             result.append(l2.val)
    #             l2 = l2.next
    #     return result

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None

        node = ListNode(0)
        start = None

        while l1 or l2:
            if not l1 and l2:
                node.val = l2.val
                l2 = l2.next
            elif l1 and not l2:
                node.val = l1.val
                l1 = l1.next
            elif l1.val < l2.val:
                node.val = l1.val
                l1 = l1.next
            else:
                node.val = l2.val
                l2 = l2.next
            if not start:
                start = node
            if l1 or l2:
                node.next = ListNode(0)
                node = node.next
            else:
                node.next = None
        return start


a = ListNode(1, next=ListNode(2, next=ListNode(4)))
b = ListNode(1, next=ListNode(3, next=ListNode(4)))
sol = Solution()
print(sol.mergeTwoLists(a, b))
a = sol.mergeTwoLists(a, b)
a = sol.mergeTwoLists(None, ListNode())
# assert sol.mergeTwoLists(a, b) == [1, 1, 2, 3, 4, 4]
# assert sol.mergeTwoLists([], []) == []
# assert sol.mergeTwoLists([], [0]) == [0]
# assert sol.mergeTwoLists([1], []) == [1]
