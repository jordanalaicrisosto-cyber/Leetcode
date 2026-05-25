import Solution
from ListNode import ListNode

test = Solution.Solution()

#Case 1
n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(0)
n4 = ListNode(-4)
pn = n1
pn.next = n2
pn = pn.next
pn.next = n3
pn = pn.next
pn.next = n4
pn = pn.next
pn.next = n2
print(test.hasCycle(n1))

#Case 2
n1 = ListNode(1)
n0 = n1
pn = n0
pn.next = n2
pn = pn.next
pn.next = n1
print(test.hasCycle(n0))

#Case 3
print(test.hasCycle(ListNode(1))) #pos=-1, result=false
