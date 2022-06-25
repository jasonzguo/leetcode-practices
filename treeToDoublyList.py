"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。
要求不能创建任何新的节点，只能调整树中节点指针的指向。

特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，
树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。
"""

"""
# Definition for a Node.
class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
"""
class Solution:
	def __init__(self):
		self.head = None
		self.tail = None

	def dfs(self, root: 'Node') -> 'Node':
		if not root:
			return None

		self.dfs(root.left)

		if self.tail:
			root.left = self.tail
			self.tail.right = root
		else:
			self.head = root
		self.tail = root

		self.dfs(root.right)



	def treeToDoublyList(self, root: 'Node') -> 'Node':
		if not root: 
			return None

		self.dfs(root)

		# cur_node = self.head
		# while cur_node:
		# 	print("cur_node.val: %d, left.val: %d, right.val: %d" % (
		# 	cur_node.val, cur_node.left.val if cur_node.left else -1, cur_node.right.val if cur_node.right else -1))
		# 	cur_node = cur_node.right

		self.head.left = self.tail
		self.tail.right = self.head
		# print(self.head.val, self.tail.val)
		return self.head