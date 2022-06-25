"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例 1：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]

示例 3：
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

import sure
from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode(l1.val + l2.val)
        result = l3

        if l3.val >= 10:
            l3.val = l3.val - 10
            l3.next = ListNode(1)

        while l1.next or l2.next:
            if l3.next:
                l3 = l3.next
            else:
                l3.next = ListNode(0)

            if l1.next and l2.next:
                l1 = l1.next
                l2 = l2.next
                l3.val = l1.val + l2.val + l3.val
            elif l1.next:
                l1 = l1.next
                l3.val = l1.val + l3.val
            elif l2.next:
                l2 = l2.next
                l3.val = l2.val + l3.val

            if l3.val >= 10:
                l3.val = l3.val - 10
                l3.next = ListNode(1)

        return result
