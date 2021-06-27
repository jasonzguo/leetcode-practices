"""
    Problem:
        Construct Binary Tree from Inorder and Postorder Traversal

    Lessons Learned:
        inorder: left, root, right
        preorder: root, left, right
        postorder: left, right, root
"""

import sure

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        node_count = len(inorder)
        return self.solve(preorder, inorder, 0, node_count - 1, 0)

    def solve(self, preorder, inorder, start_index, end_index, preorder_root_index):
        if (start_index > end_index):
            return None

        value = preorder[preorder_root_index]
        node = TreeNode(value)

        if (start_index == end_index):
            return node

        inorder_root_index = inorder.index(value)

        node.left = self.solve(preorder, inorder,
                               start_index, inorder_root_index - 1, preorder_root_index + 1)

        left_sub_tree_node_count = inorder_root_index - start_index
        node.right = self.solve(preorder, inorder,
                                inorder_root_index + 1, end_index, preorder_root_index + left_sub_tree_node_count + 1)

        return node


solution = Solution()
solution.buildTree([9, 3, 15, 20, 7],
                   [9, 15, 7, 20, 3])
