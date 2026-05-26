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
root = TreeNode()
print(test.maxDepth(root)) #2
