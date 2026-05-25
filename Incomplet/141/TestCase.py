import Solution
from ListNode import ListNode

test = Solution.Solution()

#Case 1
test.hasCycle(ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))) #pos=1, result=true

#Case 2
test.hasCycle(ListNode(1)) #pos=-1, result=false

#Case 3
test.hasCycle(ListNode(1), ListNode(2)) #pos=0, result=true
