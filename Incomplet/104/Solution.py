from TreeNode import TreeNode
from typing import Optional

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None :
            return 0

        if root.left and root.right == None :
            return 1
        list_node = []
        list_node.append(root)
        depth = 0
        nb_nodes = 0
        while list_node != [] :

            depth += 1

            size_level = len(list_node)

            for i in range(1, size_level+1) :
                node_actual = list_node.pop()
                assert -100 <= node_actual.val <= 100

                if node_actual.left != None :
                    list_node.append(node_actual.left)
                    nb_nodes += 1

                if node_actual.left != None :
                    list_node.append(node_actual.left)
                    nb_nodes += 1

        assert nb_nodes <= 104
        return depth
