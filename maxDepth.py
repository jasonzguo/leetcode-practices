"""
输入一棵二叉树的根节点，求该树的深度。
从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

提示：
节点总数 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import sure
from lib.treeNode import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)


root = TreeNode(None)
root.direct_insert_multi([3, 9, 20, None, None, 15, 7])

solution = Solution()
solution.maxDepth(root).should.equal(3)
