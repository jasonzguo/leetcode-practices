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
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        root_value = postorder[-1]
        root_index = inorder.index(root_value)
        left_index = root_index - 1
        right_index = root_index + 1

        root_node = TreeNode(root_value)
        left_node = TreeNode(inorder[left_index])
        right_node = TreeNode(inorder[right_index])
        
        while left_index - 1 > 0:
            left_node = 
        

    def preorder(self):
        pass


solution = Solution()
solution.buildTree([9, 3, 15, 20, 7],
                   [9, 15, 7, 20, 3]).pressorder().should.equal(
                       [3, 9, 20, 15, 7])
