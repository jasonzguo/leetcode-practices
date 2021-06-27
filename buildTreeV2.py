"""
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]

返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

前序遍历 preorder = [3,9,20,15,1,7]
中序遍历 inorder = [9,3,1,15,20,7]

返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
  /
  1
限制：

0 <= 节点个数 <= 5000

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

        inorder_value_index = inorder.index(value)

        node.left = self.solve(inorder, preorder,
                               start_index, inorder_value_index - 1, preorder_root_index + 1)

        node.right = self.solve(inorder, preorder,
                                inorder_value_index + 1, end_index, preorder_root_index + (inorder_value_index - start_index) + 1)

        return node


solution = Solution()
solution.buildTree([3, 9, 20, 15, 7],
                   [9, 3, 15, 20, 7])
