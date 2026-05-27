from TreeNode import TreeNode
from typing import Optional

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None :
            return 0
        if root.left == None and root.right == None :
            return 1

        list_node = []
        list_node.insert(0, root)
        depth = 0
        nb_nodes = 0
        while list_node != [] :

            size_level = len(list_node)

            for i in range(1, size_level+1) :
                node_actual = list_node.pop()

                if node_actual.left != None :
                    assert -100 <= node_actual.val <= 100
                    list_node.insert(0, node_actual.left)
                    nb_nodes += 1

                if node_actual.right != None :
                    assert -100 <= node_actual.val <= 100
                    list_node.insert(0, node_actual.right)
                    nb_nodes += 1

            depth += 1

        assert nb_nodes <= 10**4
        return depth
