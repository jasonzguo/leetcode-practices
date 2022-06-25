"""
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，
每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

示例 1:
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]

示例 2:
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]

示例 2:
输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]

提示:
-10000 <= Node.val <= 10000
Node.random 为空（null）或指向链表中的节点。
节点数目不超过 1000 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Node:
	def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
		self.val = int(x)
		self.next = next
		self.random = random

class Solution:
	def copyRandomList(self, head: 'Node') -> 'Node':
		if not head:
			 return None

		head_copy = Node(x = head.val)

		cur_node = head
		cur_node_copy = head_copy

		nodes_dict = {}
		nodes_dict[cur_node] = [cur_node_copy]

		temp_nodes = []

		while cur_node:
			if cur_node.next:
				cur_node_copy.next = Node(cur_node.next.val)
					
			if cur_node.random:
				cur_node_copy.random = cur_node.random
				temp_nodes.append(cur_node_copy)
					
			cur_node = cur_node.next
			cur_node_copy = cur_node_copy.next
			nodes_dict[cur_node] = [cur_node_copy]

		while len(temp_nodes):
			temp_node = temp_nodes.pop()
			temp_node.random = nodes_dict[temp_node.random]

		return head_copy

