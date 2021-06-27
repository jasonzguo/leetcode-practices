"""
https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/
"""

# Definition for singly-linked list.

from lib.listNode import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if (headA is None) or (headB is None):
            return None

        a_nodes_count = 0
        a_cur_node = headA
        while a_cur_node is not None:
            a_nodes_count += 1
            a_cur_node = a_cur_node.next

        b_nodes_count = 0
        b_cur_node = headB
        while b_cur_node is not None:
            b_nodes_count += 1
            b_cur_node = b_cur_node.next

        a_cur_node = headA
        while a_nodes_count > b_nodes_count:
            a_cur_node = a_cur_node.next
            a_nodes_count -= 1

        b_cur_node = headB
        while b_nodes_count > a_nodes_count:
            b_cur_node = b_cur_node.next
            b_nodes_count -= 1

        while a_cur_node is not None:
            if a_cur_node == b_cur_node:
                return a_cur_node

            a_cur_node = a_cur_node.next
            b_cur_node = b_cur_node.next

        return None


solution = Solution()

common = ListNode(None)
common.from_list([8, 4, 5])

head_a = ListNode(None)
head_a.from_list([4, 1])
head_a + common

head_b = ListNode(None)
head_b.from_list([5, 0, 1])
head_b + common

print(solution.getIntersectionNode(head_a, head_b))
