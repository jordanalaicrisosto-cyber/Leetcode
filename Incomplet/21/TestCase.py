import Solution
from ListNode import ListNode

test = Solution.Solution()

#Case 1
print(test.mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4))))) #[1,1,2,3,4,4]

#Case 2
print(test.mergeTwoLists(None, None)) #[]

#Case 3
print(test.mergeTwoLists(None, ListNode())) #[0]
