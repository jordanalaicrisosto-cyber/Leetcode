import Solution
from ListNode import ListNode

test = Solution.Solution()

#Case 1
test.mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4)))) #[1,1,2,3,4,4]

#Case 2
test.mergeTwoLists(None, None) #[]

#Case 3
test.mergeTwoLists(None, ListNode()) #[0]

#Case 4
test.mergeTwoLists(ListNode(2), ListNode(1)) #[1,2]

#Case 5
test.mergeTwoLists(ListNode(-9, ListNode(3)), ListNode(5, ListNode(7))) #[1,2]
