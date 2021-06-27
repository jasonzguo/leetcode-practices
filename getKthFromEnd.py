"""
输入一个链表，输出该链表中倒数第k个节点。
为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。

例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。
这个链表的倒数第 3 个节点是值为 4 的节点。

示例：
给定一个链表: 1->2->3->4->5, 和 k = 3.
返回链表 4->5.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        left_node = head
        right_node = head

        for _ in range(k):
            right_node = right_node.next

        while right_node is not None:
            left_node = left_node.next
            right_node = right_node.next

        return left_node
