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

    def solve(self, root: TreeNode) -> int:
        if root is not None and self.ans == True:
            left_depth = self.solve(root.left)
            right_depth = self.solve(root.right)
            if abs(left_depth - right_depth) > 1:
                self.ans = False
            return 1 + max(left_depth, right_depth)
        return 0

    def isBalanced(self, root: TreeNode) -> bool:
        self.ans = True
        self.solve(root)
        return self.ans


solution = Solution()

root_a = TreeNode(None)
root_a.direct_insert_multi([3, 9, 20, None, None, 15, 7])
solution.isBalanced(root_a).should.equal(True)

root_b = TreeNode(None)
root_b.direct_insert_multi([1, None, 3, 2])
solution.isBalanced(root_b).should.equal(False)

root_c = TreeNode(None)
root_c.direct_insert_multi([1, 2, 2, 3, None, None, 3, 4, None, None, 4])
solution.isBalanced(root_c).should.equal(False)

root_d = TreeNode(None)
root_d.direct_insert_multi(
    [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])
solution.isBalanced(root_d).should.equal(False)

root_e = TreeNode(None)
root_e.direct_insert_multi(
    [1, 2, 2, 3, 3, None, None, 4, 4])
solution.isBalanced(root_e).should.equal(False)
