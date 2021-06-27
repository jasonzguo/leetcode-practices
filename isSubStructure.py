"""
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:
	 3
	/ \
   4   5
  / \
 1   2

给定的树 B：

   4 
  /
 1

返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：
输入：A = [1,2,3], B = [3,1]
输出：false

示例 2：
输入：A = [3,4,5,1,2], B = [4,1]
输出：true

限制：
0 <= 节点个数 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import sure
from lib.treeNode import TreeNode

class Solution:
	def compare(self, A: TreeNode, B: TreeNode):
		if not A and not B:
			return True
		if A and not B:
			return True
		if not A and B:
			return False
		if A.val != B.val:
			return False

		left_equal = self.compare(A.left, B.left)
		right_equal = self.compare(A.right, B.right)
		return left_equal and right_equal

	def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
		if not A or not B:
			return False

		result = False
		nodes_a = [A]

		while len(nodes_a) > 0:
			node_a = nodes_a.pop(0)
			if node_a.val == B.val:
				result = self.compare(node_a, B)

			if result == False:
				if node_a.left:
					nodes_a.append(node_a.left)
				if node_a.right:
					nodes_a.append(node_a.right)
			else:
				break

		return result

if __name__ == '__main__':
	solution = Solution()

	root_a = TreeNode(None)
	root_a.direct_insert_multi([1, 2, 3])
	root_b = TreeNode(None)
	root_b.direct_insert_multi([3, 1])
	solution.isSubStructure(root_a, root_b).should.equal(False)

	root_a = TreeNode(None)
	root_a.direct_insert_multi([3,4,5,1,2])
	root_b = TreeNode(None)
	root_b.direct_insert_multi([4,1])
	solution.isSubStructure(root_a, root_b).should.equal(True)

	root_a = TreeNode(None)
	root_a.direct_insert_multi([10,12,6,8,3,11])
	root_b = TreeNode(None)
	root_b.direct_insert_multi([10,12,6,8])
	solution.isSubStructure(root_a, root_b).should.equal(True)