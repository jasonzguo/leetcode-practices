class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def from_list(self, l):
        cur_node = self
        for ele in l:
            if self.val is None:
                self.val = ele
            else:
                cur_node.next = ListNode(ele)
                cur_node = cur_node.next

    def reverse(self):
        prev_node = None
        cur_node = self

        while cur_node is not None:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node

        return prev_node

    def __add__(self, other):
        cur_node = self
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = other

    def __str__(self):
        s = ""
        cur_node = self
        while cur_node is not None:
            s += str(cur_node.val) + " "
            cur_node = cur_node.next
        return s
