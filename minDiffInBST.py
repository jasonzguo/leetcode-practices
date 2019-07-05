"""
    Problem:
        Minimum Value Difference between any 2 BST nodes

    Lessons Learned:
        - using inorder traversal to walk through BST
"""

import sys
import sure


class BST:
    def __init__(self, node):
        self.root = node

    def insert(self, node):
        current_node = self.root
        while (True):
            if current_node.val < node.val:
                if current_node.right is None:
                    current_node.right = node
                    break
                else:
                    current_node = current_node.right
            else:
                if current_node.left is None:
                    current_node.left = node
                    break
                else:
                    current_node = current_node.left

    def __str__(self):
        result = ''
        remaining_nodes = [self.root]
        while len(remaining_nodes) > 0:
            current_node = remaining_nodes.pop()
            result = result + str(current_node.val) + ' '
            if current_node.left is not None:
                remaining_nodes.insert(0, current_node.left)
            if current_node.right is not None:
                remaining_nodes.insert(0, current_node.right)
        return result


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(root):
    if root.left:
        inorder(root.left)
    print(root.val)
    if root.right:
        inorder(root.right)


class Solution(object):
    result = sys.maxsize
    previous_val = None
    bst = None

    def build_bst(self, numbers):
        bst = BST(Node(numbers[0]))
        for number in numbers[1:]:
            bst.insert(Node(number))

        self.result = sys.maxsize
        self.previous_val = None
        self.bst = bst

        return self

    def min_diff_in_bst(self, root=None):
        root = root if root is not None else self.bst.root

        if root.left:
            self.min_diff_in_bst(root.left)

        if self.previous_val is not None:
            # update result value
            self.result = min(self.result, root.val - self.previous_val)
        # store the privous node value
        self.previous_val = root.val

        if root.right:
            self.min_diff_in_bst(root.right)

        return self.result


solution = Solution()
solution.build_bst([4, 2, 6, 1, 3]).min_diff_in_bst().should.equal(1)
solution.build_bst([4, 2, 6]).min_diff_in_bst().should.equal(2)
solution.build_bst([7, 3]).min_diff_in_bst().should.equal(4)
solution.build_bst([32, 30, 54, 48, 78]).min_diff_in_bst().should.equal(2)

print('ok')
