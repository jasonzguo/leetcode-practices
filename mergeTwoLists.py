"""
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

限制：
0 <= 链表长度 <= 1000
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        l1_cur = l1
        l2_cur = l2

        while (l1_cur is not None) and (l2_cur is not None):
            l1_next = l1_cur.next
            l2_next = l2_cur.next

            if l1_cur.val <= l2_cur.val:
                l1_cur.next = l2_cur
                l1_cur = l1_cur.next
                l2_cur = l1_next
            elif l1_cur.val > l2_cur.val:
                l2_cur.next = l1_cur
                l2_cur = l2_next

        if l1_cur is None:
            return l1
        else:
            return l2


5, 1 - 3 - 4
3 - 4, 1 - 5
