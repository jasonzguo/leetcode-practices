"""
Given a 2D board and a word,
find if the word exists in the grid.

The word can be constructed from letters of
sequentially adjacent cell, where "adjacent" cells
are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.
"""

import sure


class WordTree:
    def __init__(self):
        self.nodes = {}

    def add_new_node(self, node):
        if node.id not in self.nodes:
            self.nodes[node.id] = node


class WordTreeNode:
    def __init__(self, value, row_index, column_index):
        self.id = value + row_index + column_index
        self.value = value
        self.row_index = row_index
        self.column_index = column_index
        self.top = None
        self.right = None
        self.bottom = None
        self.left = None

    def get_neighbours_with_value(self, value):
        neighbours = []
        if self.top and self.top.value == value:
            neighbours.append(self.top)
        if self.right and self.right.value == value:
            neighbours.append(self.right)
        if self.bottom and self.bottom.value == value:
            neighbours.append(self.bottom)
        if self.left and self.left.value == value:
            neighbours.append(self.left)
        return neighbours

    def __eq__(self, other):
        """overrides the default"""
        return self.id == other.id


class Solution:
    def build_word_tree(self, board):
        word_tree = WordTree()
        board_height = len(board)
        board_width = len(board[0])
        for row_index in range(0, board_height):
            for column_index in range(0, board_width):
                current_node = WordTreeNode(
                    board[row_index][column_index], row_index, column_index)
                word_tree.add_new_node(current_node)
                # top
                if (row_index - 1 >= 0):
                    top_node = WordTreeNode(
                        board[row_index - 1][column_index], row_index - 1, column_index)
                    current_node.top = top_node
                    word_tree.add_new_node(top_node)
                # right
                if (column_index + 1 < board_width):
                    right_node = WordTreeNode(
                        board[row_index][column_index + 1], row_index, column_index + 1)
                    current_node.right = right_node
                    word_tree.add_new_node(right_node)
                # bottom
                if (row_index + 1 < board_height):
                    bottom_node = WordTreeNode(
                        board[row_index + 1][column_index], row_index + 1, column_index)
                    current_node.bottom = bottom_node
                    word_tree.add_new_node(bottom_node)
                # left
                if (column_index - 1 >= 0):
                    left_node = WordTreeNode(
                        board[row_index, column_index - 1], row_index, column_index - 1)
                    current_node.left = left_node
                    word_tree.add_new_node(left_node)
        return word_tree

    def exist(self, board, word):
        word_tree = self.build_word_tree(board)
        word_length = len(word)
        for _, node in word_tree.nodes.items():
            char_index = 0
            if (node.value == word[char_index]):
                char_index += 1
                if char_index == word_length:
                    return True

                # DFS
                neighbours = node.get_neighbours_with_value(word[char_index])


solution = Solution()
board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

solution.exist(board, 'ABCCED')

# solution.exist(board, 'ABCCED').should.equal(True)
# solution.exist(board, 'SEE').should.equal(True)
# solution.exist(board, 'ABCB').should.equal(False)
