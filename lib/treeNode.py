class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert(self, val):
        cur = self

        if self.val is None:
            self.val = val
        else:
            while True:
                if val < cur.val:
                    if cur.left is None:
                        cur.left = TreeNode(val)
                        break
                    cur = cur.left
                elif val >= cur.val:
                    if cur.right is None:
                        cur.right = TreeNode(val)
                        break
                    cur = cur.right

    def insert_multi(self, vals):
        for val in vals:
            self.insert(val)

    def direct_insert_multi(self, vals):
        nodes = [self]
        vals_clone = vals[:]

        while len(nodes) > 0 and len(vals_clone) > 0:
            node = nodes.pop(0)

            if node.val is None and len(vals_clone) > 0:
                val = vals_clone.pop(0)
                node.val = val
            if node.left is None and len(vals_clone) > 0:
                val = vals_clone.pop(0)
                if val is not None:
                    node.left = TreeNode(val)
                    nodes.append(node.left)
            if node.right is None and len(vals_clone) > 0:
                val = vals_clone.pop(0)
                if val is not None:
                    node.right = TreeNode(val)
                    nodes.append(node.right)

    def print_inorder(self, root):
        if root:
            self.print_inorder(root.left)
            print(root.val)
            self.print_inorder(root.right)

    def print_inorder_reverse(self, root):
        if root:
            self.print_inorder_reverse(root.right)
            print(root.val)
            self.print_inorder_reverse(root.left)

    def print_preorder(self, root):
        if root is not None:
            print(root.val)
            self.print_inorder(root.left)
            self.print_inorder(root.right)

    def __str__(self):
        if self.val:
            if self.left and self.right:
                return "value: {0}, left: {1}, right: {2}".format(self.val, self.left.val, self.right.val)
            elif self.left:
                return "value: {0}, left: {1}, right: None".format(self.val, self.left.val)
            else:
                return "value: {0}, left: None, right: {1}".format(self.val, self.right.val)
        return "None"


if __name__ == "__main__":
    root = TreeNode(None)
    root.direct_insert_multi([1, None, 3, 2])
