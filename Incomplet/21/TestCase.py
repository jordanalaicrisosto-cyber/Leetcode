import Solution

test = Solution.Solution()

#Case 1
print(test.mergeTwoLists([1,2,4], [1,3,4])) #[1,1,2,3,4,4]

#Case 2
print(test.mergeTwoLists([], [])) #[]

#Case 3
print(test.mergeTwoLists([], [0])) #[0]