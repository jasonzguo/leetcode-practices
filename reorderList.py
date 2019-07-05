"""
    Problem:
        Reorder Linked List
    
    Lessons Learned:
        - finding the middle of a linked list
        - reversing a linked list
        - merging/break a linked list
"""

import sure

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class LinkedList(object):
    def __init__(self, head):
        self.head = head

    def add(self, node):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = node

    def __str__(self):
        s = ''
        current_node = self.head
        while current_node:
            s = s + str(current_node.val) + ' '
            current_node = current_node.next
        return s


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    llist = None

    def build_linked_list(self, numbers):
        if len(numbers) > 0:
            self.llist = LinkedList(Node(numbers[0]))
            for number in numbers[1:]:
                self.llist.add(Node(number))
        else:
            self.llist = LinkedList(None)
        return self

    def get_mid(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self, head):
        prev = None
        current = head

        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev

    def merge(self, head_a, head_b):
        while head_b:
            head_a_next = head_a.next
            head_b_next = head_b.next

            head_a.next = head_b
            head_b.next = head_a_next

            head_a = head_a_next
            head_b = head_b_next

    def reorder_list(self, head=None):
        head = head if head is not None else self.llist.head

        if head and head.next:
            prev = self.get_mid(head)
            mid = prev.next
            prev.next = None

            head_a = head
            head_b = self.reverse(mid)

            self.merge(head_a, head_b)

        return self

    def stringify(self, head=None):
        head = head if head is not None else self.llist.head

        s = ''
        current_node = head
        while current_node:
            s = s + str(current_node.val)
            if current_node.next:
                s += ' '
            current_node = current_node.next
        return s


solution = Solution()
solution.build_linked_list([]).reorder_list().stringify().should.equal('')
solution.build_linked_list([1,
                            2]).reorder_list().stringify().should.equal('1 2')
solution.build_linked_list(
    [1, 2, 3]).reorder_list().stringify().should.equal('1 3 2')
solution.build_linked_list(
    [1, 2, 3, 4]).reorder_list().stringify().should.equal('1 4 2 3')
solution.build_linked_list(
    [1, 2, 3, 4, 5]).reorder_list().stringify().should.equal('1 5 2 4 3')

print('ok')