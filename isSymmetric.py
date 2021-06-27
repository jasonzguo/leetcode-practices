"""
请实现一个函数，用来判断一棵二叉树是不是对称的。
如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true

示例 2：
输入：root = [1,2,2,null,3,null,3]
输出：false
 
限制：
0 <= 节点个数 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def areNodesEqual(self, node_a, node_b):
        if node_a == node_b:
            return True

        if (node_a is None) and (node_b is not None):
            return False
        elif (node_a is not None) and (node_b is None):
            return False
        elif node_a.val != node_b.val:
            return False
        return True

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        if self.areNodesEqual(root.left, root.right) == False:
            return False

        nodes = [root.left, root.right]
        while len(nodes) > 0:
            left = nodes.pop(0)
            right = nodes.pop(0)

            if left == right == None:
                continue

            if self.areNodesEqual(left, right) == False:
                return False
            if self.areNodesEqual(left.left, right.right) == False:
                return False
            if self.areNodesEqual(left.right, right.left) == False:
                return False

            nodes.append(left.left)
            nodes.append(right.right)
            nodes.append(left.right)
            nodes.append(right.left)
        return True
