"""
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
 
限制：

0 <= 节点个数 <= 5000
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return head

        nodes_stack = []
        current_node = head

        while current_node is not None:
            nodes_stack.append(current_node)
            current_node = current_node.next

        new_head = nodes_stack[-1]
        while len(nodes_stack) > 0:
            node = nodes_stack.pop()

            if len(nodes_stack) == 0:
                node.next = None
            else:
                node.next = nodes_stack[-1]

        return new_head

    def reverseListPointers(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return head

        prev_node = None
        cur_node = head
        while cur_node is not None:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node

        return cur_node
