import Solution
from TreeNode import TreeNode

test = Solution.Solution()

#Case 1
root = TreeNode(
    3,
    TreeNode(
        9,
        None,
        None),
    TreeNode(20,
             TreeNode(15,
                      None,
                      None),
             TreeNode(7,
                      None,
                      None))
    )

print(test.maxDepth(root)) #3

#Case 2
root = TreeNode(1,
                None,
                TreeNode(2,
                         None,
                         None))
print(test.maxDepth(root)) #2


#Case 3
root = TreeNode(0,
                None,
                None)
print(test.maxDepth(root)) #1

#Case 4
root = TreeNode(1,
                TreeNode(2,
                         None,
                         None),
                None)
print(test.maxDepth(root)) #2

#Case 5
root = TreeNode(1,
                TreeNode(2,
                         TreeNode(4,
                                  None,
                                  None),
                        None),
                TreeNode(3,
                         None,
                         TreeNode(5,
                                  None,
                                  None)))
print(test.maxDepth(root)) #3
