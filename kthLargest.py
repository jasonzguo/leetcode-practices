"""
给定一棵二叉搜索树，请找出其中第k大的节点。

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4

示例 2:
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
 
限制：
1 ≤ k ≤ 二叉搜索树元素个数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sure
from lib.treeNode import TreeNode


class Solution:
    def dfs(self, root, nodes, k):
        if root is not None:
            self.dfs(root.right, nodes, k)
            if len(nodes) < k:
                nodes.append(root)
                self.dfs(root.left, nodes, k)

    def kthLargest(self, root: TreeNode, k: int) -> int:
        nodes = []
        self.dfs(root, nodes, k)
        return nodes[-1].val


root = TreeNode(None)
root.insert_multi([5, 3, 6, 2, 4, 1, 8])
# root.print_inorder_reverse(root)

solution = Solution()
solution.kthLargest(root, 2).should.equal(6)
