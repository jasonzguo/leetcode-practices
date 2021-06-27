"""
  输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        result = []

        cur_node = head
        while (cur_node is not None):
            stack.append(cur_node.val)
            cur_node = cur_node.next

        while (len(stack) > 0):
            result.append(stack.pop())

        return result
