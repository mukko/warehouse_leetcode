from typing import List, TypeVar

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        result_tail = result

        over = False
        while l1 != None or l2 != None or over:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            cul = val1 + val2
            if over:
                cul += 1
                over = False

            if cul >= 10:
                cul = cul % 10
                over = True

            result_tail.next = ListNode(cul)
            result_tail = result_tail.next
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
            
        return result.next

l11 = ListNode(2)
l12 = ListNode(4)
l13 = ListNode(3)

l21 = ListNode(5)
l22 = ListNode(6)
l23 = ListNode(4)

l11.next = l12
l12.next = l13

l21.next = l22
l22.next = l23

solution = Solution()
result = solution.addTwoNumbers(l11, l21)

print(result)
while result != None:
    print(result.val)
    result = result.next

