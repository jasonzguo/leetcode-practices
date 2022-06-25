"""
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。
如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

示例 1:
给定二叉树 [3,9,20,None,None,15,7]
    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:
给定二叉树 [1,2,2,3,3,None,None,4,4]
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

限制：
0 <= 树的结点个数 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import sure
from typing import List
from lib.treeNode import TreeNode


class Solution:
    def __init__(self):
        self.ans = True

    def get_height(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left_height = self.get_height(root.left)
        if left_height == -1:
            return -1
        right_height = self.get_height(root.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) >= 2:
            return -1
        return max(left_height, right_height) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True

        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        
        if abs(left_height - right_height) >= 2:
            return False
        if left_height == -1:
            return False
        if right_height == -1:
            return False
        return True
        



solution = Solution()

root_a = TreeNode(None)
root_a.direct_insert_multi([3, 9, 20, None, None, 15, 7])
solution.isBalanced(root_a).should.equal(True, 'wrong 1')

root_b = TreeNode(None)
root_b.direct_insert_multi([1, None, 3, 2])
solution.isBalanced(root_b).should.equal(False, 'wrong 2')

root_c = TreeNode(None)
root_c.direct_insert_multi([1, 2, 2, 3, 3, None, None, 4, 4])
solution.isBalanced(root_c).should.equal(False, 'wrong 3')

root_d = TreeNode(None)
root_d.direct_insert_multi(
    [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])
solution.isBalanced(root_d).should.equal(False, 'wrong 4')

root_e = TreeNode(None)
root_e.direct_insert_multi(
    [1, 2, 2, 3, 3, None, None, 4, 4])
solution.isBalanced(root_e).should.equal(False, 'wrong 5')
